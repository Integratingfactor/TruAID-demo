# 🧠 MCP Blockchain Tool (Agent Logging + Anchoring)

This toolset enables agents to log signed contexts and anchor them into a tamper-evident blockchain. You can interact with the system via `curl` or through the `mcp` CLI.

---

## 🚀 1. Start the TruAID Blockchain Node

```bash
 (source .env; python tool-blockchain-services/blockchain_node.py )
```

Expected output:

```
INFO - Starting Blockchain Node on http://127.0.0.1:3000

```

## 🤖 2. Start the TruAID MCP Server

```bash
 (source .env; python mcp-server/mcp_server.py )
```

Expected output:

```
INFO - Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

```


## ⛓ 3. Interact with TruAID Blockchain

### Submit new context to Blockchain

```
(source .env; python tests/cli_mcp_client.py mcp-submit-context \
  "agent-001" \
  "sha256:abc123" \
  "sha256:in456" \
  "sha256:out789" \
  "policy:default-v1" \
  "0xsigexample")
```


✅ Expected:

```
[
  {
    "status": "context received",
    "count": 1
  }
]
```


### Anchor Logs to Blockchain

```
 (source .env; python tests/cli_mcp_client.py mcp-force-anchor) 
```

✅ Expected:

```
[
  {
    "block_hash": "70c13f6870bcd5e368d2221527d7d294ab4ab1f958330aa8ec1993e0935fbfe0",
    "index": 1,
    "status": "anchored"
  }
]
```


### Inspect the Blockchain Chain

```
(source .env; python tests/cli_mcp_client.py mcp-get-chain)
```


✅ Expected:

```
[
  {
    "index": 0,
    "timestamp": "2025-07-13 06:29:18.833917",
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "081cb8a55fe29bc16d2ea04a5e519150cb8433379414bf20ff994e4cfe92f05b",
    "nonce": 0
  },
  {
    "index": 1,
    "timestamp": "2025-07-13 06:50:30.825789",
    "data": {
      "mcp_merkle_root": "cc6f16092543ee48b339485b9509d4846fa6f533b73b8aa8e96e3e65957ef70f",
      "log_count": 1
    },
    "previous_hash": "081cb8a55fe29bc16d2ea04a5e519150cb8433379414bf20ff994e4cfe92f05b",
    "hash": "c0f37e5ae875e90e5077ee34089f56e6ff95c200405af4dd50277e7afd1df4b4",
    "nonce": 0
  }
]
```

### Verify Blockchain Integrity

```
(source .env; python tests/cli_mcp_client.py mcp-validate-chain)
```

✅ Expected:

```
[
  {
    "valid": true
  }
]
```

## Validation Logic
Each block:

Hashes all fields (index, timestamp, data, previous hash, nonce)

Points to previous block’s hash

The /valid check verifies:

block.hash == block.compute_hash()

block[i].previous_hash == block[i-1].hash
