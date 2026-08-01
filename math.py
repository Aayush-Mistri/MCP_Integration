from fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int , b:int)->int:
    """_summary_

        Add two numbers

    """
    return a + b


@mcp.tool()
def multiply(a:int , b:int)->int:
    """_summary_

        multiply two numbers

    """
    return a * b

## The transport="stdio" argument tells the server to :
##    Use standard input/output(stdin and stdout) to receive and respond to tool funcion calls
if __name__ == "__main__":
    mcp.run(transport="stdio") 
