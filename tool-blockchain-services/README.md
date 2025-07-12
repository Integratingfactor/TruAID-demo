# 🛠 Blockchain Tool Server for MCP Context Logging

This project provides a simple blockchain-backed log anchoring tool for Model Context Protocol (MCP) agents. It receives context logs, anchors them to an internal blockchain, and supports validation and inspection.

---

## 🚀 1. Start the Server

```bash
python blockchain_tool.py
```

You should see output like:

```
INFO - Starting Blockchain Tool server on http://127.0.0.1:8000
```


## 2. Submit Agent Context

Use curl to POST an agent-generated context to /submit-context:

```
curl -X POST http://127.0.0.1:8000/submit-context \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "agent-001",
    "model_digest": "sha256:abc123",
    "input_hash": "sha256:in456",
    "output_hash": "sha256:out789",
    "policy_id": "policy:default-v1",
    "timestamp": "2025-07-12T23:00:00Z",
    "signature": "0xsigexample"
}'
```



✅ Expected Response:

```
{
  "status": "context received",
  "count": 1
}
```


## 🔐 3. Anchor Logs to Blockchain

When logs are ready (or periodically), anchor them into the blockchain:

```
curl -X POST http://127.0.0.1:8000/force-anchor

```


✅ Expected Response:

```
{
  "status": "anchored",
  "block_hash": "<sha256-hash>",
  "index": 1
}

```

## 🔎 4. Inspect the Blockchain

View the full blockchain:

```
curl http://127.0.0.1:8000/chain

```

Each block contains:

```
index

timestamp

data (including mcp_merkle_root, log_count)

previous_hash

hash

nonce
```


## ✅ 5. Verify Blockchain Integrity

Check if the chain is still valid:

```
curl http://127.0.0.1:8000/valid

```

Expected result:

```
{
  "valid": true
}

```

## 🛡 How Validation Works


The /valid endpoint checks:

- ✅ block.hash == block.compute_hash()

- ✅ block[i].previous_hash == block[i-1].hash


If any mismatch is detected, it logs the error and returns:

```
{"valid": false}

```



