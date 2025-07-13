from google.adk.agents import Agent
from .prompt import PROMPT

service_agent = Agent(
        name="service_agent_writing",
        model="gemini-2.5-flash-preview-05-20",
        description=(
            "A demo service agent that writes stories."
            ),
        instruction=PROMPT
    )
