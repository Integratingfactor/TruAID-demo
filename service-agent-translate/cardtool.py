import os, json
from google.adk.tools import ToolContext

def get_agent_card():
    agent_path = os.path.join(os.path.dirname(__file__), ".well-known", "agent.json")
    with open(agent_path, "r", encoding="utf-8") as f:
        agent_data = json.load(f)
    return agent_data

def memorize(key: str, value: str, tool_context: ToolContext):
    """
    Memorize pieces of information, one key-value pair at a time.

    Args:
        key: the label indexing the memory to store the value.
        value: the information to be stored.
        tool_context: The ADK tool context.

    Returns:
        A status message.
    """
    mem_dict = tool_context.state
    mem_dict[key] = value
    return {"status": f'Stored "{key}": "{value}"'}
