from fastapi import FastAPI
import weave
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from .cardtool import get_agent_card as get_agent_card_tool
from service_agent_translate.agent import root_agent  # Ensure agent is imported to register it

USER_ID = "user_id_1234"
APP_NAME = "hiring_agent"

app = FastAPI()
# PII ignore, reference: https://weave-docs.wandb.ai/guides/tracking/redact-pii/
weave.init("TruAID", settings={"redact_pii": True, "redact_pii_fields":["CREDIT_CARD", "US_SSN"]})

session_service = InMemorySessionService()

class HireTask(BaseModel):
    text: str

@weave.op()
@app.post("/hire")
async def submit_translation_task(task: HireTask):
    if not task.text:
        raise HTTPException(status_code=400, detail="Text must be provided")
    session=await session_service.create_session(
                    user_id=USER_ID, app_name=APP_NAME)
    adk_runner = Runner(session_service=session_service,
                    agent=root_agent,
                    app_name="hiring_agent")
    # Prepare the user's message in ADK format
    content = types.Content(role='user', parts=[types.Part(text=task.text)])

    full_response_text = ""  # To accumulate all parts of the response

    # Key Concept: run_async executes the agent logic and yields Events.
    # We iterate through events to find the final answer.
    try:
        async for event in adk_runner.run_async(
            user_id=USER_ID, session_id=session.id,
            new_message=content
        ):
            # # accumulate the full response text if needed
            # if event.content and event.content.parts:
            #     full_response_text += ''.join(part.text for part in event.content.parts if part.text)
            if event.error_message:
                full_response_text += f"\n[Event] Author: {event.author}, Type: Error, Message: {event.error_message}\n"


            # Key Concept: is_final_response() marks the concluding message for the turn.
            if event.is_final_response():
                ### in case of SSE / streaming, partial response is being collected
                if event.content and event.content.parts:
                    # full_response_text += "\n" + ''.join(part.text for part in event.content.parts if part.text)
                    full_response_text = event.content.parts[0].text
                if event.actions and event.actions.escalate:  # Handle potential errors/escalations
                    full_response_text += f"\nAgent escalated: {event.error_message or 'No specific message.'}\n"
                #### in case of SSE, we just keep looping until run_async does EOF and loop ends itself
                #### no need to explicitly break the loop
                # if event.turn_complete:
                #     logger.info("Turn complete, returning response to user.")
                #     break  # Stop processing events once the final response is found
            else:
                if event.partial and event.content and event.content.parts:
                    text = ''.join(part.text for part in event.content.parts if part.text)
                    full_response_text += text
                elif event.actions and event.actions.transfer_to_agent:
                    full_response_text += f"\n{event.author} transferring to {event.actions.transfer_to_agent} ...\n"
                elif event.get_function_calls():
                    for function in event.get_function_calls():
                        full_response_text += f"\n{event.author} calling function: {function.name} ...\n" if function.name != "transfer_to_agent" else ""

    except Exception as e:
        raise e

    # The agent's final response is returned as a string.
    return {"translated_text": full_response_text}

@app.get("/.well-known/agent.json")
async def get_agent_card():
    return get_agent_card_tool()


