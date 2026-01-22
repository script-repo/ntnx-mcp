"""MCP Server implementation for Nutanix Prism Central."""

import asyncio
import json
import sys
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    TextContent,
    Tool,
)

from ntnx_mcp.client import PrismCentralClient
from ntnx_mcp.config import Settings, get_settings
from ntnx_mcp.executor import ToolExecutor
from ntnx_mcp.tools.registry import get_all_tools


def create_server(settings: Settings) -> tuple[Server, ToolExecutor]:
    """Create and configure the MCP server."""
    server = Server("ntnx-mcp")
    client = PrismCentralClient(settings)
    executor = ToolExecutor(client)

    all_tools = get_all_tools()
    for tool in all_tools:
        executor.register_tool(tool)

    @server.list_tools()  # type: ignore[untyped-decorator,no-untyped-call]
    async def list_tools() -> list[Tool]:
        """Return the list of available tools."""
        return [
            Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=tool["inputSchema"],
            )
            for tool in all_tools
        ]

    @server.call_tool()  # type: ignore[untyped-decorator]
    async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
        """Execute a tool and return the result."""
        result = await executor.execute(name, arguments or {})

        if "error" in result:
            error = result["error"]
            error_text = f"Error: {error.get('message', 'Unknown error')}"
            if error.get("details"):
                error_text += f"\nDetails: {error['details']}"
            if error.get("status_code"):
                error_text += f"\nStatus: {error['status_code']}"
            return [TextContent(type="text", text=error_text)]

        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    return server, executor


async def run_server() -> None:
    """Run the MCP server."""
    settings = get_settings()

    if not settings.has_credentials:
        print(
            "Error: No credentials configured. Set both PRISM_CENTRAL_USERNAME "
            "and PRISM_CENTRAL_PASSWORD.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Starting Nutanix MCP server for {settings.host}:{settings.port}", file=sys.stderr)

    server, executor = create_server(settings)

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


def main() -> None:
    """Entry point for the MCP server."""
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\nShutting down...", file=sys.stderr)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
