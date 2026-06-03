from mcp.server.fastmcp import FastMCP

from tools import (
    get_top_protocols_by_tvl,
    get_protocol_info,
    get_top_chains
)

mcp = FastMCP(
    "Crypto Research MCP"
)

#Tool registration
@mcp.tool()
def top_protocols(limit: int = 10):
    return get_top_protocols_by_tvl(limit)

@mcp.tool()
def protocol_info(name: str):
    return get_protocol_info(name)

@mcp.tool()
def top_chains(limit: int = 10):
    return get_top_chains(limit)

#Run Server
if __name__ == "__main__":
    mcp.run()
