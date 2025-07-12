# 🧠 MCP Blockchain Tool (Agent Logging + Anchoring)

This toolset enables agents to log signed contexts and anchor them into a tamper-evident blockchain. You can interact with the system via `curl` or through the `mcp` CLI.

---

## 🚀 1. Start the Blockchain Tool Server

```bash
python blockchain_tool.py
```

Expected output:

```
INFO - Starting Blockchain Tool server on http://127.0.0.1:8000

```


## 🤖 2. Submit Agent Context
▶️
 With mcp CLI:

```
mcp call tool submit_context --input '{
  "agent_id": "agent-001",
  "model_digest": "sha256:abc123",
  "input_hash": "sha256:in456",
  "output_hash": "sha256:out789",
  "policy_id": "policy:default-v1",
  "timestamp": "2025-07-12T23:00:00Z",
  "signature": "0xsigexample"
}'
```


✅ Expected:

```
{"status": "context received", "count": 1}

```


## ⛓ 3. Anchor Logs to Blockchain
▶️ With mcp CLI:

```
mcp call tool force_anchor

```

✅ Response:

```
{
  "status": "anchored",
  "block_hash": "<sha256-hash>",
  "index": 1
}

```


## 🔍 4. Inspect the Blockchain Chain
▶️ With mcp CLI:

```
mcp call tool get_blockchain_chain

```


🔎 View fields:

```
index

timestamp

mcp_merkle_root

previous_hash

hash

nonce

```

## 🛡 5. Verify Blockchain Integrity
▶️ With mcp CLI:

```
mcp call tool validate_blockchain

```

✅ Returns:

```
{"valid": true}

```

✔️ Validation Logic
Each block:

Hashes all fields (index, timestamp, data, previous hash, nonce)

Points to previous block’s hash

The /valid check verifies:

block.hash == block.compute_hash()

block[i].previous_hash == block[i-1].hash



