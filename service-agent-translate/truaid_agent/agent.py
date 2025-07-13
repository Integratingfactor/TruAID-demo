from google.adk.agents import Agent
from .prompt import PROMPT
from .truaid import generate_agent_context
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

truaid_agent = Agent(
        name="truaid_agent_translate",
        model="gemini-2.5-flash-preview-05-20",
        description=(
            "A demo agent that helps with TruAID blockchain operations"
            ),
        instruction=PROMPT,
        tools=[generate_agent_context, MCPToolset(
            connection_params=StreamableHTTPConnectionParams(url="http://127.0.0.1:8000/mcp")
        )],
    )