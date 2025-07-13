from google.adk.agents import Agent
from .prompt import PROMPT

service_agent = Agent(
        name="service_agent_programming",
        model="gemini-2.5-flash-preview-05-20",
        description=(
            "A demo service agent that took programming tasks."
            ),
        instruction=PROMPT
    )
