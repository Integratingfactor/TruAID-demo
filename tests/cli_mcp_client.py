import requests
import argparse
import json

MCP_SERVER_URL = "http://127.0.0.1:3000"

def submit_mcp_context(agent_id, model_digest, input_hash, output_hash, policy_id, timestamp, signature):
    url = f"{MCP_SERVER_URL}/submit-context"
    payload = {
        "agent_id": agent_id,
        "model_digest": model_digest,
        "input_hash": input_hash,
        "output_hash": output_hash,
        "policy_id": policy_id,
        "timestamp": timestamp,
        "signature": signature
    }
    response = requests.post(url, json=payload)
    print(response.json())

def get_mcp_chain():
    url = f"{MCP_SERVER_URL}/chain"
    response = requests.get(url)
    print(json.dumps(response.json(), indent=2))

def validate_mcp_chain():
    url = f"{MCP_SERVER_URL}/valid"
    response = requests.get(url)
    print(response.json())

def force_mcp_anchor():
    url = f"{MCP_SERVER_URL}/force-anchor"
    response = requests.post(url)
    print(response.json())

def main():
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
        submit_mcp_context(args.agent_id, args.model_digest, args.input_hash, args.output_hash, args.policy_id, args.timestamp, args.signature)
    elif args.command == "mcp-get-chain":
        get_mcp_chain()
    elif args.command == "mcp-validate-chain":
        validate_mcp_chain()
    elif args.command == "mcp-force-anchor":
        force_mcp_anchor()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
