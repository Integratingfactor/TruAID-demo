# mcp_blockchain_server.py

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
import requests
from typing import List
import logging
import contextlib
from fastapi import FastAPI
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("mcp-blockchain-server")

# Initialize MCP server
mcp = FastMCP("Blockchain Tool MCP")

# Tool server endpoint (e.g., your blockchain tool microservice)
TOOL_SERVER_URL = "http://127.0.0.1:3000"

# === Data Models ===
class MCPContext(BaseModel):
    agent_id: str
    model_digest: str
    input_hash: str
    output_hash: str
    policy_id: str
    timestamp: str
    signature: str

class AnchorResult(BaseModel):
    block_hash: str = Field(..., description="Hash of the anchored block")
    index: int = Field(..., description="Block index in the chain")
    status: str = Field(..., description="Result status")

class ChainBlock(BaseModel):
    index: int
    timestamp: str
    data: dict | str
    previous_hash: str
    hash: str
    nonce: int

# === MCP Tools ===

@mcp.tool()
def submit_context(context: MCPContext) -> dict:
    """Submit a signed MCP context to the blockchain log tool."""
    logger.info(f"[submit_context] Submitting context for agent {context.agent_id} at {context.timestamp}")
    response = requests.post(f"{TOOL_SERVER_URL}/submit-context", json=context.dict())
    logger.info(f"[submit_context] Tool server response: {response.status_code} {response.text}")
    return response.json()

@mcp.tool()
def force_anchor() -> AnchorResult:
    """Force anchoring of current logs into the blockchain."""
    logger.info("[force_anchor] Forcing log anchoring...")
    response = requests.post(f"{TOOL_SERVER_URL}/force-anchor")
    logger.info(f"[force_anchor] Anchor response: {response.status_code} {response.text}")
    if response.status_code != 200:
        logger.error("[force_anchor] Anchor failed")
        raise RuntimeError("Anchor failed: " + response.text)
    return AnchorResult(**response.json())

@mcp.tool()
def get_blockchain_chain() -> List[ChainBlock]:
    """Fetch the full blockchain from the backend."""
    logger.info("[get_blockchain_chain] Fetching blockchain chain")
    response = requests.get(f"{TOOL_SERVER_URL}/chain")
    logger.info(f"[get_blockchain_chain] Chain fetch status: {response.status_code}")
    return [ChainBlock(**b) for b in response.json()]

@mcp.tool()
def validate_blockchain() -> dict:
    """Validate the current state of the blockchain."""
    logger.info("[validate_blockchain] Validating blockchain")
    response = requests.get(f"{TOOL_SERVER_URL}/valid")
    logger.info(f"[validate_blockchain] Validation status: {response.status_code} | Response: {response.text}")
    return response.json()

# # === Run MCP Server ===
# # Create a combined lifespan to manage both session managers
# @contextlib.asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with contextlib.AsyncExitStack() as stack:
#         await stack.enter_async_context(mcp.run(transport="streamable-http"))
#         yield

# app = FastAPI(lifespan=lifespan)
app = FastAPI()
mcp.run(transport="streamable-http")
app.mount("/", mcp.streamable_http_app())


if __name__ == "__main__":
    logger.info("[startup] Starting MCP Blockchain Tool server on host 0.0.0.0, port 3000...")
    uvicorn.run(app, host="127.0.0.1", port=3000)
    # # Run the FastMCP server with Streamable HTTP transport
    # mcp.run(transport="streamable_http", http_stream={"port": 3000})
