import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("omc")

OMC_MCP_ENDPOINT = os.environ.get(
    "OMC_MCP_ENDPOINT", "http://127.0.0.1:8000/api/experimental/mcp"
)
OMC_API_TOKEN = os.environ.get("OMC_API_TOKEN")


async def fetch_current_question():
    headers = {"Authorization": f"Bearer {OMC_API_TOKEN}", "Accept": "application/json"}
    url = f"{OMC_MCP_ENDPOINT}/current_question"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_current_question(state: str) -> str:
    url = f"{OMC_MCP_ENDPOINT}/current_question"
    question = await fetch_current_question()
    if question is None:
        return "Failed to fetch current question."
    return question


@mcp.tool()
async def ping(state: str) -> str:
    return "pong"


if __name__ == "__main__":
    mcp.run(transport="stdio")
