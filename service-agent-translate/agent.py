from google.adk.agents import Agent
from .prompt import PROMPT
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

root_agent = Agent(
        name="service_agent_translate",
        model="gemini-2.5-flash-preview-05-20",
        description=(
            "A demo service agent that translates user's english text into a target language."
            ),
        instruction=PROMPT,
        tools=[MCPToolset(
            connection_params=StreamableHTTPConnectionParams(url="http://127.0.0.1:8000/mcp")
        )],
    )