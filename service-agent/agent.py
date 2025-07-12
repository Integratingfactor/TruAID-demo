from google.adk.agents import Agent
from .prompt import PROMPT

root_agent = Agent(
    name="demo_service_agent",
    model="gemini-2.5-flash-preview-05-20",
    description=(
        "A demo service agent that translates user's english text into a target language."
        ),
    instruction=PROMPT,
    tools=[],
)
