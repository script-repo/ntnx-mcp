"""Tests for tool registry and definitions."""

import pytest
from ntnx_mcp.tools.registry import get_all_tools, ToolRegistry


def test_get_all_tools_returns_list():
    """Test that get_all_tools returns a list."""
    tools = get_all_tools()
    assert isinstance(tools, list)
    assert len(tools) > 0


def test_all_tools_have_required_fields():
    """Test that all tools have required fields."""
    tools = get_all_tools()
    for tool in tools:
        assert "name" in tool, f"Tool missing name: {tool}"
        assert "description" in tool, f"Tool {tool.get('name')} missing description"
        assert "inputSchema" in tool, f"Tool {tool.get('name')} missing inputSchema"
        assert "metadata" in tool, f"Tool {tool.get('name')} missing metadata"


def test_all_tools_have_valid_input_schema():
    """Test that all tools have valid input schemas."""
    tools = get_all_tools()
    for tool in tools:
        schema = tool["inputSchema"]
        assert schema.get("type") == "object", f"Tool {tool['name']} schema must be object type"
        assert "properties" in schema, f"Tool {tool['name']} schema missing properties"


def test_all_tools_have_namespace_metadata():
    """Test that all tools have namespace in metadata."""
    tools = get_all_tools()
    for tool in tools:
        metadata = tool["metadata"]
        assert "namespace" in metadata, f"Tool {tool['name']} missing namespace"
        assert "entity" in metadata, f"Tool {tool['name']} missing entity"
        assert "operation" in metadata, f"Tool {tool['name']} missing operation"


def test_vmm_tools_exist():
    """Test that VMM tools are defined."""
    tools = ToolRegistry.vmm_tools()
    tool_names = [t["name"] for t in tools]
    assert "vmm_list" in tool_names
    assert "vmm_get" in tool_names
    assert "vmm_create" in tool_names
    assert "vmm_power_on" in tool_names
    assert "vmm_power_off" in tool_names


def test_clustermgmt_tools_exist():
    """Test that cluster management tools are defined."""
    tools = ToolRegistry.clustermgmt_tools()
    tool_names = [t["name"] for t in tools]
    assert "clustermgmt_clusters_list" in tool_names
    assert "clustermgmt_cluster_get" in tool_names


def test_networking_tools_exist():
    """Test that networking tools are defined."""
    tools = ToolRegistry.networking_tools()
    tool_names = [t["name"] for t in tools]
    assert "networking_subnets_list" in tool_names
    assert "networking_subnet_create" in tool_names


def test_monitoring_tools_exist():
    """Test that monitoring tools are defined."""
    tools = ToolRegistry.monitoring_tools()
    tool_names = [t["name"] for t in tools]
    assert "monitoring_alerts_list" in tool_names
    assert "monitoring_alert_acknowledge" in tool_names


def test_tool_names_are_unique():
    """Test that all tool names are unique."""
    tools = get_all_tools()
    names = [t["name"] for t in tools]
    assert len(names) == len(set(names)), "Duplicate tool names found"


def test_vmm_create_has_required_params():
    """Test that vmm_create has correct required parameters."""
    tools = ToolRegistry.vmm_tools()
    vmm_create = next(t for t in tools if t["name"] == "vmm_create")
    required = vmm_create["inputSchema"].get("required", [])
    assert "name" in required
    assert "cluster_id" in required
