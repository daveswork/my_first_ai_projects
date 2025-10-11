from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv


# Create an MCP server

mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",
    port=8050
)


# Add a simple calculator tool
@mcp.tool()
def add(a: int, b:int) -> int:
    """
    Add two numbers together
    """
    return a+b

# Need to add the following ENV variables
#  export ALLOWED_ORIGINS=http://192.168.5.7:6274
#  export DANGEROUSLY_OMIT_AUTH=true
#  export HOST=0.0.0.0
# TODO:
# - Change transport to StreamableHttp

if __name__ == "__main__":
    transport = "http"
    if transport == "stdio":
        print("Running the server with stdio transport.")
        mcp.run(transport="stdio")
    elif transport == "http":
        print("Running server with SSE transport.")
        mcp.run(transport="http")
    else:
        raise ValueError(f"Unknown transport: {transport}")
