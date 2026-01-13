# Usage Guide

## Overview

The Nutanix MCP Server exposes Prism Central v4 API operations as tools that AI agents can invoke. Each tool corresponds to an API operation within a namespace.

## Tool Naming Convention

Tools follow the pattern: `{namespace}_{operation}`

Examples:
- `vmm_list` - List VMs
- `vmm_get` - Get a specific VM
- `vmm_create` - Create a VM
- `vmm_power_on` - Power on a VM
- `clustermgmt_list` - List clusters
- `networking_list` - List networks

---

## Common Operations

### List Virtual Machines

```
List all VMs in the cluster
```

With filtering (OData):
```
List VMs where the name contains "prod"
```

### Get VM Details

```
Get details for VM with ID abc123-def456-...
```

### Power Operations

```
Power on VM "web-server-01"
Power off VM "test-vm" 
```

### Create a VM

```
Create a VM named "new-web-server" with 4 vCPUs, 8GB RAM, on cluster "production-cluster"
```

### List Clusters

```
Show all clusters managed by this Prism Central
```

### List Networks

```
List all networks available for VM deployment
```

### Get Alerts

```
Show all critical alerts from the last 24 hours
```

### List Storage Containers

```
List all storage containers and their available space
```

---

## Namespace Reference

### Virtual Machine Management (`vmm`)

| Tool | Description |
|------|-------------|
| `vmm_list` | List VMs with optional filtering |
| `vmm_get` | Get VM by ID |
| `vmm_create` | Create a new VM |
| `vmm_update` | Update VM configuration |
| `vmm_delete` | Delete a VM |
| `vmm_power_on` | Power on a VM |
| `vmm_power_off` | Power off a VM |
| `vmm_reset` | Reset a VM |
| `vmm_suspend` | Suspend a VM |
| `vmm_resume` | Resume a suspended VM |
| `vmm_snapshot_create` | Create VM snapshot |
| `vmm_snapshot_list` | List VM snapshots |
| `vmm_clone` | Clone a VM |

### Cluster Management (`clustermgmt`)

| Tool | Description |
|------|-------------|
| `clustermgmt_list` | List clusters |
| `clustermgmt_get` | Get cluster details |
| `clustermgmt_hosts_list` | List hosts in clusters |
| `clustermgmt_host_get` | Get host details |

### Networking (`networking`)

| Tool | Description |
|------|-------------|
| `networking_subnets_list` | List subnets |
| `networking_subnet_get` | Get subnet details |
| `networking_subnet_create` | Create subnet |
| `networking_vpc_list` | List VPCs |
| `networking_floating_ip_list` | List floating IPs |

### Storage (`storage`)

| Tool | Description |
|------|-------------|
| `storage_containers_list` | List storage containers |
| `storage_container_get` | Get container details |

### Monitoring (`monitoring`)

| Tool | Description |
|------|-------------|
| `monitoring_alerts_list` | List alerts |
| `monitoring_alert_get` | Get alert details |
| `monitoring_alert_acknowledge` | Acknowledge alert |
| `monitoring_alert_resolve` | Resolve alert |
| `monitoring_events_list` | List events |
| `monitoring_audits_list` | List audit logs |

### Data Protection (`dataprotection`)

| Tool | Description |
|------|-------------|
| `dataprotection_policies_list` | List protection policies |
| `dataprotection_policy_get` | Get policy details |
| `dataprotection_recovery_points_list` | List recovery points |

### Identity & Access Management (`iam`)

| Tool | Description |
|------|-------------|
| `iam_users_list` | List users |
| `iam_user_get` | Get user details |
| `iam_roles_list` | List roles |
| `iam_directory_services_list` | List directory services |

### Flow Management (`microseg`)

| Tool | Description |
|------|-------------|
| `microseg_policies_list` | List security policies |
| `microseg_policy_get` | Get policy details |
| `microseg_address_groups_list` | List address groups |
| `microseg_service_groups_list` | List service groups |

### Lifecycle Management (`lifecycle`)

| Tool | Description |
|------|-------------|
| `lifecycle_updates_list` | List available updates |
| `lifecycle_inventory_get` | Get LCM inventory |

### Prism (`prism`)

| Tool | Description |
|------|-------------|
| `prism_tasks_list` | List tasks |
| `prism_task_get` | Get task status |
| `prism_categories_list` | List categories |

---

## OData Filtering

Many list operations support OData query parameters:

### Filter Examples

```
# Exact match
filter: "name eq 'my-vm'"

# Contains
filter: "contains(name, 'prod')"

# Multiple conditions
filter: "powerState eq 'ON' and numVcpus gt 4"

# Date filtering
filter: "createdTime gt 2024-01-01T00:00:00Z"
```

### Sorting

```
orderby: "name asc"
orderby: "createdTime desc"
```

### Pagination

```
top: 50
skip: 100
```

### Field Selection

```
select: "name,powerState,numVcpus,memoryBytes"
```

---

## Error Handling

The server returns structured errors:

```json
{
  "error": {
    "code": "AUTHENTICATION_FAILED",
    "message": "Invalid credentials",
    "details": "Check username and password"
  }
}
```

Common error codes:
- `AUTHENTICATION_FAILED` - Invalid credentials
- `NOT_FOUND` - Resource doesn't exist
- `PERMISSION_DENIED` - Insufficient permissions
- `RATE_LIMITED` - Too many requests
- `VALIDATION_ERROR` - Invalid input parameters
- `CONNECTION_ERROR` - Cannot reach Prism Central

---

## Async Operations

Long-running operations (create, update, delete) return a task ID:

```json
{
  "taskId": "abc123-def456-...",
  "status": "PENDING",
  "message": "VM creation initiated"
}
```

Check task status:
```
Get status of task abc123-def456-...
```

---

## Best Practices

1. **Use filters** - Filter on the server side for better performance
2. **Limit results** - Use `top` parameter to limit large result sets
3. **Check tasks** - Monitor async task completion for create/update/delete
4. **Handle errors** - The AI will receive error context for troubleshooting
5. **Use IDs** - When working with specific resources, use the external ID (UUID)
