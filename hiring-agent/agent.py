from google.adk.agents import Agent
from .prompt import PROMPT
from .truaid_agent.agent import truaid_agent
root_agent = Agent(
        name="root_agent_translate",
        model="gemini-2.5-flash-preview-05-20",
        description=(
            "A demo hiring agent for discovering agents on the TruAID blockchain and hiring them for tasks specified by the user."
            ),
        instruction=PROMPT,
        sub_agents=[truaid_agent],
    )
