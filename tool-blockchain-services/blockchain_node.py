# blockchain_tool_server.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from hashlib import sha256
from datetime import datetime
import uvicorn
import json
import threading
import logging

# === Logging Setup ===
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("blockchain-tool-server")

# === Blockchain Basics ===
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        logger.info("Creating genesis block")
        genesis = Block(0, str(datetime.utcnow()), "Genesis Block", "0")
        self.chain.append(genesis)

    def latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        logger.info("Adding new block with data: %s", data)
        previous_block = self.latest_block()
        new_block = Block(len(self.chain), str(datetime.utcnow()), data, previous_block.hash)
        self.chain.append(new_block)
        logger.info("New block added at index %d with hash %s", new_block.index, new_block.hash)
        return new_block

    def is_valid(self):
        logger.info("Validating blockchain...")
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                logger.error("Block %d has invalid hash", current.index)
                return False
            if current.previous_hash != previous.hash:
                logger.error("Block %d has mismatched previous hash", current.index)
                return False
        logger.info("Blockchain is valid")
        return True


# === MCP Payload ===
class MCPContext(BaseModel):
    agent_id: str
    agent_card: str
    model_digest: str
    input_hash: str
    output_hash: str
    policy_id: str
    timestamp: str
    signature: str


# === FastAPI Tool Server ===
app = FastAPI()
blockchain = Blockchain()
log_pool: List[MCPContext] = []

@app.post("/submit-context")
def submit_context(ctx: MCPContext):
    logger.info("Received context submission from agent %s", ctx.agent_id)
    log_pool.append(ctx)
    logger.info("Current log pool size: %d", len(log_pool))
    return {"status": "context received", "count": len(log_pool)}

@app.get("/chain")
def get_chain():
    logger.info("Returning blockchain with %d blocks", len(blockchain.chain))
    return [block.__dict__ for block in blockchain.chain]

@app.get("/valid")
def validate_chain():
    is_valid = blockchain.is_valid()
    return {"valid": is_valid}

@app.post("/force-anchor")
def force_anchor():
    global log_pool
    if not log_pool:
        logger.info("No logs to anchor")
        return {"status": "no logs to anchor"}
    logger.info("Anchoring %d logs", len(log_pool))
    combined_hash = sha256("".join(sorted([json.dumps(log.dict(), sort_keys=True) for log in log_pool])).encode()).hexdigest()
    block = blockchain.add_block({
        "mcp_merkle_root": combined_hash,
        "agent_cards": [log.agent_card for log in log_pool],
        "log_count": len(log_pool)
    })
    log_pool = []
    return {
        "status": "anchored",
        "block_hash": block.hash,
        "index": block.index
    }

# === Entry Point ===
if __name__ == "__main__":
    logger.info("Starting Blockchain Node on http://127.0.0.1:3000")
    uvicorn.run(app, host="127.0.0.1", port=3000)

