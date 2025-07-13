import datetime, json
from google.adk.tools import ToolContext

def generate_agent_context(agent_id: str, tool_context: ToolContext) -> dict:
    """
    Generate a context dictionary for the given agent_id.

    :param agent_id: The ID of the agent.
    :return: A dictionary containing the context information.
    """
    model_digest = "sha256:abc123"  # Example model digest
    input_hash = "sha256:in456"     # Example input hash
    output_hash = "sha256:out789"   # Example output hash
    policy_id = "policy:default-v1" # Example policy ID
    signature = "0xsigexample"      # Example signature
    mem_dict = tool_context.state

    context = {
        "agent_id": agent_id,
        # "agent_card": json.dumps(mem_dict.get("agent_card", '{"error": "agent_card not found in memory"}')),  # Fetch from memory
        "agent_card": mem_dict.get('agent_card', {'error': 'agent_card not found in memory'}),
        "model_digest": model_digest,
        "input_hash": input_hash,
        "output_hash": output_hash,
        "policy_id": policy_id,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat() + "Z",
        "signature": signature
    }
    return context
