"""Tool execution logic - translates MCP tool calls to API requests."""

import uuid
from typing import Any, Optional

from ntnx_mcp.client import PrismCentralClient, PrismCentralError


class ToolExecutor:
    """Executes MCP tool calls against the Prism Central API."""

    def __init__(self, client: PrismCentralClient):
        self.client = client
        self._tools: dict[str, dict[str, Any]] = {}

    def register_tool(self, tool: dict[str, Any]) -> None:
        """Register a tool definition."""
        self._tools[tool["name"]] = tool

    def get_tool(self, name: str) -> Optional[dict[str, Any]]:
        """Get a tool definition by name."""
        return self._tools.get(name)

    async def execute(self, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        """Execute a tool and return the result."""
        tool = self.get_tool(tool_name)
        if not tool:
            return {"error": {"code": "UNKNOWN_TOOL", "message": f"Unknown tool: {tool_name}"}}

        metadata = tool.get("metadata", {})
        namespace = metadata.get("namespace")
        entity = metadata.get("entity")
        operation = metadata.get("operation")

        if not namespace or not entity:
            return {
                "error": {
                    "code": "INVALID_TOOL",
                    "message": "Tool missing namespace/entity metadata",
                }
            }

        try:
            if operation == "list":
                return await self._execute_list(namespace, entity, arguments)
            elif operation == "get":
                return await self._execute_get(namespace, entity, metadata, arguments)
            elif operation == "get_single":
                return await self._execute_get_single(namespace, entity, arguments)
            elif operation == "create":
                return await self._execute_create(namespace, entity, tool_name, arguments)
            elif operation == "delete":
                return await self._execute_delete(namespace, entity, metadata, arguments)
            elif operation == "action":
                return await self._execute_action(namespace, entity, metadata, arguments)
            else:
                return {
                    "error": {
                        "code": "UNKNOWN_OPERATION",
                        "message": f"Unknown operation: {operation}",
                    }
                }
        except PrismCentralError as e:
            return {
                "error": {
                    "code": e.__class__.__name__.upper().replace("ERROR", "_ERROR"),
                    "message": e.message,
                    "status_code": e.status_code,
                    "details": e.details,
                }
            }
        except Exception as e:
            return {"error": {"code": "INTERNAL_ERROR", "message": str(e)}}

    async def _execute_list(
        self, namespace: str, entity: str, arguments: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute a list operation."""
        return await self.client.list(
            namespace=namespace,
            path=entity,
            filter=arguments.get("filter"),
            orderby=arguments.get("orderby"),
            top=arguments.get("top"),
            skip=arguments.get("skip"),
            select=arguments.get("select"),
            expand=arguments.get("expand"),
        )

    async def _execute_get(
        self, namespace: str, entity: str, metadata: dict[str, Any], arguments: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute a get operation."""
        id_param = metadata.get("id_param", "id")
        entity_id = arguments.get(id_param)
        if not entity_id:
            return {
                "error": {
                    "code": "MISSING_PARAM",
                    "message": f"Missing required parameter: {id_param}",
                }
            }

        return await self.client.get(
            namespace=namespace,
            path=entity,
            entity_id=entity_id,
            select=arguments.get("select"),
            expand=arguments.get("expand"),
        )

    async def _execute_get_single(
        self, namespace: str, entity: str, arguments: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute a get operation for a singleton resource."""
        return await self.client.request("GET", namespace, entity)

    async def _execute_create(
        self, namespace: str, entity: str, tool_name: str, arguments: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute a create operation."""
        body = self._build_create_body(tool_name, arguments)
        request_id = str(uuid.uuid4())
        return await self.client.create(
            namespace=namespace,
            path=entity,
            body=body,
            request_id=request_id,
        )

    async def _execute_delete(
        self, namespace: str, entity: str, metadata: dict[str, Any], arguments: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute a delete operation."""
        id_param = metadata.get("id_param", "id")
        entity_id = arguments.get(id_param)
        if not entity_id:
            return {
                "error": {
                    "code": "MISSING_PARAM",
                    "message": f"Missing required parameter: {id_param}",
                }
            }

        request_id = str(uuid.uuid4())
        return await self.client.delete(
            namespace=namespace,
            path=entity,
            entity_id=entity_id,
            request_id=request_id,
        )

    async def _execute_action(
        self, namespace: str, entity: str, metadata: dict[str, Any], arguments: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute an action on an entity."""
        id_param = metadata.get("id_param", "id")
        action = metadata.get("action")
        entity_id = arguments.get(id_param)

        if not entity_id:
            return {
                "error": {
                    "code": "MISSING_PARAM",
                    "message": f"Missing required parameter: {id_param}",
                }
            }
        if not action:
            return {
                "error": {
                    "code": "INVALID_TOOL",
                    "message": "Tool missing action in metadata",
                }
            }

        body_args = {k: v for k, v in arguments.items() if k != id_param}
        body = body_args if body_args else None
        request_id = str(uuid.uuid4())

        return await self.client.action(
            namespace=namespace,
            path=entity,
            entity_id=entity_id,
            action=action,
            body=body,
            request_id=request_id,
        )

    def _build_create_body(self, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        """Build the request body for a create operation."""
        if tool_name == "vmm_create":
            return self._build_vm_create_body(arguments)
        elif tool_name == "networking_subnet_create":
            return self._build_subnet_create_body(arguments)
        elif tool_name == "volumes_group_create":
            return self._build_volume_group_create_body(arguments)
        else:
            return arguments

    def _build_vm_create_body(self, args: dict[str, Any]) -> dict[str, Any]:
        """Build VM creation request body."""
        body: dict[str, Any] = {
            "name": args["name"],
            "cluster": {"extId": args["cluster_id"]},
        }

        if args.get("num_vcpus"):
            body["numSockets"] = 1
            body["numCoresPerSocket"] = args["num_vcpus"]

        if args.get("memory_gb"):
            body["memorySizeBytes"] = int(args["memory_gb"] * 1024 * 1024 * 1024)

        nics = []
        if args.get("subnet_id"):
            nics.append({
                "networkInfo": {
                    "subnet": {"extId": args["subnet_id"]}
                }
            })
        if nics:
            body["nics"] = nics

        disks = []
        if args.get("disk_size_gb") or args.get("image_id"):
            disk: dict[str, Any] = {"diskAddress": {"busType": "SCSI", "index": 0}}
            if args.get("image_id"):
                disk["backingInfo"] = {
                    "vmDisk": {
                        "diskSizeBytes": int(args.get("disk_size_gb", 50) * 1024 * 1024 * 1024),
                        "dataSource": {"reference": {"extId": args["image_id"]}}
                    }
                }
            else:
                disk["backingInfo"] = {
                    "vmDisk": {
                        "diskSizeBytes": int(args["disk_size_gb"] * 1024 * 1024 * 1024),
                    }
                }
            disks.append(disk)
        if disks:
            body["disks"] = disks

        return body

    def _build_subnet_create_body(self, args: dict[str, Any]) -> dict[str, Any]:
        """Build subnet creation request body."""
        body: dict[str, Any] = {
            "name": args["name"],
            "subnetType": args["subnet_type"],
            "cluster": {"extId": args["cluster_id"]},
        }

        if args.get("vlan_id") is not None:
            body["vlanId"] = args["vlan_id"]

        if args.get("network_ip") and args.get("prefix_length"):
            body["ipConfig"] = {
                "ipv4": {
                    "ipSubnet": {
                        "ip": {"value": args["network_ip"]},
                        "prefixLength": args["prefix_length"],
                    }
                }
            }
            if args.get("gateway_ip"):
                body["ipConfig"]["ipv4"]["defaultGatewayIp"] = {"value": args["gateway_ip"]}

        return body

    def _build_volume_group_create_body(self, args: dict[str, Any]) -> dict[str, Any]:
        """Build volume group creation request body."""
        body: dict[str, Any] = {
            "name": args["name"],
            "cluster": {"extId": args["cluster_id"]},
        }
        if args.get("description"):
            body["description"] = args["description"]
        return body
