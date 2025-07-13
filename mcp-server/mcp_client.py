# mcp_client.py

import asyncio
from mcp.client import MCPClient
import json

# MCP server address (adjust if running on a different port/host)
MCP_SERVER_URL = "http://127.0.0.1:3000"

# Agent context to submit (simulates agent-signed result log)
context = {
    "agent_id": "agent-001",
    "model_digest": "sha256:abc123",
    "input_hash": "sha256:in456",
    "output_hash": "sha256:out789",
    "policy_id": "policy:default-v1",
    "timestamp": "2025-07-12T23:00:00Z",
    "signature": "0xsigexample"
}

async def main():
    # Create MCP client instance targeting local MCP HTTP server
    client = MCPClient(MCP_SERVER_URL)

    # === 1. Submit context ===
    print("\n➡️ [submit_context] Request:")
    print(json.dumps(context, indent=2))
    result = await client.call_tool("submit_context", input=context)
    print("✅ [submit_context] Result:")
    print(json.dumps(result, indent=2))

    # === 2. Force anchor ===
    print("\n➡️ [force_anchor] Request: {} (no input)")
    result = await client.call_tool("force_anchor")
    print("✅ [force_anchor] Result:")
    print(json.dumps(result, indent=2))

    # === 3. Fetch chain ===
    print("\n➡️ [get_blockchain_chain] Request: {} (no input)")
    result = await client.call_tool("get_blockchain_chain")
    print("🔗 [get_blockchain_chain] Result:")
    print(json.dumps(result, indent=2))

    # === 4. Validate blockchain ===
    print("\n➡️ [validate_blockchain] Request: {} (no input)")
    result = await client.call_tool("validate_blockchain")
    print("🛡 [validate_blockchain] Result:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
