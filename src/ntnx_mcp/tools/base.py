"""Base tool definitions and shared schemas."""

from typing import Any

ODATA_PARAMS: dict[str, Any] = {
    "filter": {
        "type": "string",
        "description": "OData filter expression (e.g., \"name eq 'my-vm'\")",
    },
    "orderby": {
        "type": "string",
        "description": "Sort field and direction (e.g., \"name asc\")",
    },
    "top": {
        "type": "integer",
        "description": "Maximum number of results to return",
    },
    "skip": {
        "type": "integer",
        "description": "Number of results to skip (for pagination)",
    },
    "select": {
        "type": "string",
        "description": "Comma-separated list of fields to return",
    },
    "expand": {
        "type": "string",
        "description": "Related entities to include",
    },
}


def create_list_tool(
    name: str,
    namespace: str,
    entity: str,
    description: str,
    extra_params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create a standard list tool definition."""
    properties = dict(ODATA_PARAMS)
    if extra_params:
        properties.update(extra_params)

    return {
        "name": name,
        "description": description,
        "inputSchema": {
            "type": "object",
            "properties": properties,
        },
        "metadata": {
            "namespace": namespace,
            "entity": entity,
            "operation": "list",
        },
    }


def create_get_tool(
    name: str,
    namespace: str,
    entity: str,
    description: str,
    id_param: str = "id",
    id_description: str = "Entity ID (UUID)",
) -> dict[str, Any]:
    """Create a standard get tool definition."""
    return {
        "name": name,
        "description": description,
        "inputSchema": {
            "type": "object",
            "properties": {
                id_param: {
                    "type": "string",
                    "description": id_description,
                },
                "select": ODATA_PARAMS["select"],
                "expand": ODATA_PARAMS["expand"],
            },
            "required": [id_param],
        },
        "metadata": {
            "namespace": namespace,
            "entity": entity,
            "operation": "get",
            "id_param": id_param,
        },
    }


def create_delete_tool(
    name: str,
    namespace: str,
    entity: str,
    description: str,
    id_param: str = "id",
    id_description: str = "Entity ID (UUID)",
) -> dict[str, Any]:
    """Create a standard delete tool definition."""
    return {
        "name": name,
        "description": description,
        "inputSchema": {
            "type": "object",
            "properties": {
                id_param: {
                    "type": "string",
                    "description": id_description,
                },
            },
            "required": [id_param],
        },
        "metadata": {
            "namespace": namespace,
            "entity": entity,
            "operation": "delete",
            "id_param": id_param,
        },
    }


def create_action_tool(
    name: str,
    namespace: str,
    entity: str,
    action: str,
    description: str,
    id_param: str = "id",
    id_description: str = "Entity ID (UUID)",
    extra_params: dict[str, Any] | None = None,
    required_params: list[str] | None = None,
) -> dict[str, Any]:
    """Create a tool for an entity action."""
    properties: dict[str, Any] = {
        id_param: {
            "type": "string",
            "description": id_description,
        },
    }
    if extra_params:
        properties.update(extra_params)

    required = [id_param]
    if required_params:
        required.extend(required_params)

    return {
        "name": name,
        "description": description,
        "inputSchema": {
            "type": "object",
            "properties": properties,
            "required": required,
        },
        "metadata": {
            "namespace": namespace,
            "entity": entity,
            "operation": "action",
            "action": action,
            "id_param": id_param,
        },
    }
