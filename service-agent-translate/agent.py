from google.adk.agents import Agent
from .prompt import PROMPT
from .service_agent.agent import service_agent
from .truaid_agent.agent import truaid_agent

root_agent = Agent(
        name="root_agent_translate",
        model="gemini-2.5-flash-preview-05-20",
        description=(
            "A demo service provider agent for translation services."
            ),
        instruction=PROMPT,
        sub_agents=[service_agent, truaid_agent],
    )