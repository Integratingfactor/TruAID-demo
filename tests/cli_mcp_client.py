import argparse
import asyncio
import json
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

# async def submit_mcp_context(session, agent_id, model_digest, input_hash, output_hash, policy_id, timestamp, signature):
async def submit_mcp_context(session):
    payload = {
        "agent_id": "agent-001",
    "model_digest": "sha256:abc123",
    "input_hash": "sha256:in456",
    "output_hash": "sha256:out789",
    "policy_id": "policy:default-v1",
    "timestamp": "2025-07-12T23:00:00Z",
    "signature": "0xsigexample"
    }
    tool_result = await session.call_tool("submit_context", payload)
    print(tool_result)

async def get_mcp_chain(session):
    tool_result = await session.call_tool("get_blockchain_chain", {})
    print(tool_result)

async def validate_mcp_chain(session):
    tool_result = await session.call_tool("validate_blockchain", {})
    print(tool_result)

async def force_mcp_anchor(session):
    tool_result = await session.call_tool("force_anchor", {})
    print(tool_result)

async def main():
    async with streamablehttp_client("http://127.0.0.1:8000/mcp") as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            parser = argparse.ArgumentParser(description="CLI for MCP Server Service")
            subparsers = parser.add_subparsers(dest="command")

            # MCP Submit context command
            mcp_submit_parser = subparsers.add_parser("mcp-submit-context", help="Submit a new MCP context")
            mcp_submit_parser.add_argument("agent_id")
            mcp_submit_parser.add_argument("model_digest")
            mcp_submit_parser.add_argument("input_hash")
            mcp_submit_parser.add_argument("output_hash")
            mcp_submit_parser.add_argument("policy_id")
            mcp_submit_parser.add_argument("timestamp")
            mcp_submit_parser.add_argument("signature")

            # MCP Get chain command
            subparsers.add_parser("mcp-get-chain", help="Get the MCP blockchain")

            # MCP Validate chain command
            subparsers.add_parser("mcp-validate-chain", help="Validate the MCP blockchain")

            # MCP Force anchor command
            subparsers.add_parser("mcp-force-anchor", help="Force anchor logs into the MCP blockchain")

            args = parser.parse_args()

            if args.command == "mcp-submit-context":
                await submit_mcp_context(session, args.agent_id, args.model_digest, args.input_hash, args.output_hash, args.policy_id, args.timestamp, args.signature)
            elif args.command == "mcp-get-chain":
                await get_mcp_chain(session)
            elif args.command == "mcp-validate-chain":
                await validate_mcp_chain(session)
            elif args.command == "mcp-force-anchor":
                await force_mcp_anchor(session)
            else:
                parser.print_help()

if __name__ == "__main__":
    asyncio.run(main())
    main()
