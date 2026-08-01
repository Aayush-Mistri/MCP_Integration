from fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def add(location:str)->str:
    """_summary_

        Get the weather locaion

    """
    return "It is sunny"

## The transport="stdio" argument tells the server to :
##    Use standard input/output(stdin and stdout) to receive and respond to tool funcion calls
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
