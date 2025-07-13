import requests
import argparse
import json

BASE_URL = "http://127.0.0.1:8000"

def submit_context(agent_id, model_digest, input_hash, output_hash, policy_id, timestamp, signature):
    url = f"{BASE_URL}/submit-context"
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

def get_chain():
    url = f"{BASE_URL}/chain"
    response = requests.get(url)
    print(json.dumps(response.json(), indent=2))

def validate_chain():
    url = f"{BASE_URL}/valid"
    response = requests.get(url)
    print(response.json())

def force_anchor():
    url = f"{BASE_URL}/force-anchor"
    response = requests.post(url)
    print(response.json())

def main():
    parser = argparse.ArgumentParser(description="CLI for Blockchain Tool Service")
    subparsers = parser.add_subparsers(dest="command")

    # Submit context command
    submit_parser = subparsers.add_parser("submit-context", help="Submit a new context")
    submit_parser.add_argument("agent_id")
    submit_parser.add_argument("model_digest")
    submit_parser.add_argument("input_hash")
    submit_parser.add_argument("output_hash")
    submit_parser.add_argument("policy_id")
    submit_parser.add_argument("timestamp")
    submit_parser.add_argument("signature")

    # Get chain command
    subparsers.add_parser("get-chain", help="Get the blockchain")

    # Validate chain command
    subparsers.add_parser("validate-chain", help="Validate the blockchain")

    # Force anchor command
    subparsers.add_parser("force-anchor", help="Force anchor logs into the blockchain")

    args = parser.parse_args()

    if args.command == "submit-context":
        submit_context(args.agent_id, args.model_digest, args.input_hash, args.output_hash, args.policy_id, args.timestamp, args.signature)
    elif args.command == "get-chain":
        get_chain()
    elif args.command == "validate-chain":
        validate_chain()
    elif args.command == "force-anchor":
        force_anchor()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
