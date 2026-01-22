# Nutanix Prism Central MCP Server

An MCP (Model Context Protocol) server that connects AI agents to Nutanix Prism Central via the v3 API.

## Features

- **Full v3 API Coverage** - Access all 18 Prism Central namespaces
- **Simple Setup** - Configure with environment variables
- **OData Support** - Filter, sort, and paginate results
- **Secure** - Supports basic auth with username/password

## Quick Start

```bash
# Install
pip install -e .

# Configure
export PRISM_CENTRAL_HOST=192.168.1.100
export PRISM_CENTRAL_USERNAME=admin
export PRISM_CENTRAL_PASSWORD=your-password
export PRISM_CENTRAL_VERIFY_SSL=false

# Run
python -m ntnx_mcp
```

## Supported Namespaces

| Namespace | Description |
|-----------|-------------|
| `vmm` | Virtual Machine Management |
| `clustermgmt` | Cluster Management |
| `networking` | Networking |
| `storage` | Storage Containers |
| `dataprotection` | Data Protection |
| `monitoring` | Alerts & Events |
| `iam` | Identity & Access |
| `microseg` | Flow Security |
| `lifecycle` | LCM Updates |
| `prism` | Tasks & Categories |
| `aiops` | AI Operations |
| `files` | Files |
| `volumes` | Volumes |
| `objects` | Object Storage |
| `licensing` | Licensing |
| `security` | Security |
| `datapolicies` | Data Policies |
| `opsmgmt` | NCM Operations |

## Client Configuration

### Amp / Claude Desktop

```json
{
  "mcpServers": {
    "nutanix": {
      "command": "python",
      "args": ["-m", "ntnx_mcp"],
      "env": {
        "PRISM_CENTRAL_HOST": "192.168.1.100",
        "PRISM_CENTRAL_USERNAME": "admin",
        "PRISM_CENTRAL_PASSWORD": "your-password"
      }
    }
  }
}
```

## Example Usage

Once connected, ask your AI agent:

- "List all VMs in the cluster"
- "Show me VMs with more than 8 vCPUs"
- "Get the status of cluster 'production'"
- "Show all critical alerts"
- "Create a VM named 'test-server' with 4 vCPUs and 8GB RAM"

## Documentation

- [Product Requirements](specs/PRD.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Usage Guide](docs/USAGE.md)

## Requirements

- Python 3.10+
- Nutanix Prism Central pc.2024.3+ (for full v3 API support)
- Network access to Prism Central (port 9440)

## License

MIT
