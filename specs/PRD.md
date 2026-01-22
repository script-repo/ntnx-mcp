# Product Requirements Document: Nutanix Prism Central MCP Server

## Overview

An MCP (Model Context Protocol) server that provides AI agents with access to Nutanix Prism Central infrastructure through the v3 API. This enables AI-powered infrastructure management, monitoring, and automation.

## Problem Statement

Infrastructure teams need to interact with Nutanix Prism Central for VM management, networking, storage, and monitoring. Current methods require direct API knowledge or UI navigation. An MCP server bridges AI assistants to Prism Central, enabling natural language infrastructure operations.

## Goals

1. **Simplicity** - Easy to deploy, configure, and use
2. **Completeness** - Support all v3 API namespaces
3. **Security** - Secure credential handling
4. **Reliability** - Robust error handling and logging

## Target Users

- Infrastructure engineers using AI coding assistants
- DevOps teams automating Nutanix operations
- IT administrators querying infrastructure state

---

## Supported Namespaces (v3 API)

The MCP server exposes tools for all 18 Nutanix v3 API namespaces:

| Namespace | Endpoint | Description |
|-----------|----------|-------------|
| **AI Ops** | `aiops` | Analysis, reporting, capacity planning, VM rightsizing, playbooks |
| **Cluster Management** | `clustermgmt` | Manage hosts, clusters, and infrastructure |
| **Data Policies** | `datapolicies` | Policies for disaster recovery and storage |
| **Data Protection** | `dataprotection` | Disaster recovery and backup solutions |
| **Files** | `files` | Virtual file servers, shares, DR/sync policies |
| **Flow Management** | `microseg` | Network security policies, address groups |
| **Identity & Access** | `iam` | User identity and access management |
| **Licensing** | `licensing` | License management and compliance |
| **Lifecycle Management** | `lifecycle` | Infrastructure and firmware upgrades |
| **Monitoring** | `monitoring` | Alerts, events, and audits |
| **Networking** | `networking` | Network configuration, AHV networking |
| **Objects Storage** | `objects` | Object store service management |
| **NCM Base Platform** | `opsmgmt` | Prism reports and operations |
| **Prism** | `prism` | Tasks, categories, batch operations |
| **Security** | `security` | Encryption, certificates, hardening |
| **Storage** | `storage` | Volume groups and storage containers |
| **Virtual Machine Management** | `vmm` | VM lifecycle management |
| **Volumes** | `volumes` | Volume group management |

---

## Functional Requirements

### FR-1: Authentication
- Support HTTP Basic Authentication (username/password)
- Credentials via environment variables
- Never log or expose credentials

### FR-2: Tool Structure
Each namespace exposes tools following this pattern:
- `{namespace}_list` - List entities with OData filtering
- `{namespace}_get` - Get entity by ID
- `{namespace}_create` - Create new entity
- `{namespace}_update` - Update existing entity
- `{namespace}_delete` - Delete entity
- Namespace-specific actions (e.g., `vmm_power_on`, `vmm_power_off`)

### FR-3: OData Support
- `$filter` - Filter results
- `$orderby` - Sort results
- `$select` - Select specific fields
- `$expand` - Include related entities
- `$top` / `$skip` - Pagination

### FR-4: Error Handling
- Return meaningful error messages
- Include HTTP status codes
- Provide actionable remediation hints
- Log errors to stderr (not stdout)

### FR-5: Response Format
- Return structured JSON responses
- Include pagination metadata
- Include task IDs for async operations

---

## Non-Functional Requirements

### NFR-1: Performance
- Connection pooling for API requests
- Request timeout configuration
- Rate limiting awareness (30-80 req/s based on PC size)

### NFR-2: Security
- TLS/SSL for all API connections
- Option to skip certificate verification (dev only)
- No credential logging

### NFR-3: Compatibility
- Python 3.10+
- Prism Central pc.2024.3+ (for full v3 API support)
- AOS 7.0+

### NFR-4: Transport
- STDIO transport (default for local use)
- Optional HTTP/SSE transport for remote deployment

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AI Agent (Amp, Claude, etc.)         │
└─────────────────────────┬───────────────────────────────┘
                          │ MCP Protocol (JSON-RPC)
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   ntnx-mcp Server                       │
│  ┌───────────────────────────────────────────────────┐  │
│  │              Tool Registry                        │  │
│  │  - vmm_list, vmm_get, vmm_create, vmm_power_on   │  │
│  │  - clustermgmt_list, clustermgmt_get             │  │
│  │  - networking_list, networking_create            │  │
│  │  - ... (all 18 namespaces)                       │  │
│  └───────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────┐  │
│  │              Prism Central Client                 │  │
│  │  - Authentication                                 │  │
│  │  - Request/Response handling                      │  │
│  │  - OData query building                          │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────┬───────────────────────────────┘
                          │ HTTPS (v3 REST API)
                          ▼
┌─────────────────────────────────────────────────────────┐
│                 Nutanix Prism Central                   │
│                    (v3 API)                             │
└─────────────────────────────────────────────────────────┘
```

---

## Configuration

Environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `PRISM_CENTRAL_HOST` | Yes | Prism Central IP or hostname |
| `PRISM_CENTRAL_USERNAME` | Yes | Username for basic auth |
| `PRISM_CENTRAL_PASSWORD` | Yes | Password for basic auth |
| `PRISM_CENTRAL_PORT` | No | Port (default: 9440) |
| `PRISM_CENTRAL_VERIFY_SSL` | No | Verify SSL certs (default: false) |

---

## Example Tool Definitions

### vmm_list
```json
{
  "name": "vmm_list",
  "description": "List virtual machines in Prism Central",
  "inputSchema": {
    "type": "object",
    "properties": {
      "filter": {
        "type": "string",
        "description": "OData filter (e.g., \"name eq 'my-vm'\")"
      },
      "orderby": {
        "type": "string",
        "description": "Sort field (e.g., \"name asc\")"
      },
      "top": {
        "type": "integer",
        "description": "Max results to return"
      },
      "select": {
        "type": "string",
        "description": "Fields to return (comma-separated)"
      }
    }
  }
}
```

### vmm_power_on
```json
{
  "name": "vmm_power_on",
  "description": "Power on a virtual machine",
  "inputSchema": {
    "type": "object",
    "properties": {
      "vm_id": {
        "type": "string",
        "description": "VM external ID (UUID)"
      }
    },
    "required": ["vm_id"]
  }
}
```

---

## Success Metrics

1. All 18 namespaces accessible via MCP tools
2. < 500ms response time for list operations
3. Clear error messages for common failures
4. Single command deployment
5. Works with Amp, Claude Desktop, and other MCP clients

---

## Out of Scope (v1)

- Prism Element (v2.0 API) - PC only
- NDB (Era) integration
- NKE (Karbon) integration  
- NCM Self-Service (Calm)
- Foundation Central
- Disaster Recovery (planned for future PC releases)

---

## Timeline

| Phase | Description | Duration |
|-------|-------------|----------|
| 1 | Core infrastructure + VMM namespace | 1 week |
| 2 | Remaining namespaces | 1 week |
| 3 | Documentation + testing | 3 days |
| 4 | Deployment packaging | 2 days |

---

## References

- [Nutanix v3 API Documentation](https://developers.nutanix.com)
- [Nutanix v3 API Introduction](https://www.nutanix.dev/api-reference-v3/)
- [MCP Specification](https://modelcontextprotocol.io/specification/latest)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
