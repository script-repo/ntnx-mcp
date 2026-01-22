"""Tool definitions for all Nutanix v3 API namespaces."""

from ntnx_mcp.tools.base import ODATA_PARAMS, create_get_tool, create_list_tool
from ntnx_mcp.tools.registry import ToolRegistry, get_all_tools

__all__ = [
    "ODATA_PARAMS",
    "create_list_tool",
    "create_get_tool",
    "ToolRegistry",
    "get_all_tools",
]
