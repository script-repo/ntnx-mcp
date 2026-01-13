# Deployment Guide

## Prerequisites

- Python 3.10 or higher
- Access to Nutanix Prism Central (pc.2024.3+ recommended)
- Prism Central credentials (username/password or API key)

## Quick Start

### 1. Install

```bash
# Clone the repository
git clone https://github.com/script-repo/ntnx-mcp.git
cd ntnx-mcp

# Install with uv (recommended)
uv pip install -e .

# Or with pip
pip install -e .
```

### 2. Configure

Create a `.env` file:

```bash
PRISM_CENTRAL_HOST=your-pc-ip-or-hostname
PRISM_CENTRAL_USERNAME=admin
PRISM_CENTRAL_PASSWORD=your-password
PRISM_CENTRAL_PORT=9440
PRISM_CENTRAL_VERIFY_SSL=true
```

Or export environment variables:

```bash
export PRISM_CENTRAL_HOST=192.168.1.100
export PRISM_CENTRAL_USERNAME=admin
export PRISM_CENTRAL_PASSWORD=secretpassword
```

### 3. Run

```bash
# Run directly
python -m ntnx_mcp

# Or with uv
uv run ntnx-mcp
```

---

## Configuration Options

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PRISM_CENTRAL_HOST` | Yes | - | Prism Central IP or FQDN |
| `PRISM_CENTRAL_USERNAME` | Yes* | - | Username for authentication |
| `PRISM_CENTRAL_PASSWORD` | Yes* | - | Password for authentication |
| `PRISM_CENTRAL_API_KEY` | Yes* | - | API key (alternative to user/pass) |
| `PRISM_CENTRAL_PORT` | No | 9440 | Prism Central API port |
| `PRISM_CENTRAL_VERIFY_SSL` | No | true | Verify SSL certificates |

*Either username/password OR API key is required

---

## Client Configuration

### Amp

Add to your MCP configuration (`.amp/mcp.json` or settings):

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

### Claude Desktop

Add to `claude_desktop_config.json`:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

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

### Using uv

```json
{
  "mcpServers": {
    "nutanix": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/ntnx-mcp", "ntnx-mcp"],
      "env": {
        "PRISM_CENTRAL_HOST": "192.168.1.100",
        "PRISM_CENTRAL_USERNAME": "admin",
        "PRISM_CENTRAL_PASSWORD": "your-password"
      }
    }
  }
}
```

---

## Docker Deployment

### Build

```bash
docker build -t ntnx-mcp .
```

### Run

```bash
docker run -it \
  -e PRISM_CENTRAL_HOST=192.168.1.100 \
  -e PRISM_CENTRAL_USERNAME=admin \
  -e PRISM_CENTRAL_PASSWORD=your-password \
  ntnx-mcp
```

### Docker Compose

```yaml
version: '3.8'
services:
  ntnx-mcp:
    build: .
    environment:
      - PRISM_CENTRAL_HOST=${PRISM_CENTRAL_HOST}
      - PRISM_CENTRAL_USERNAME=${PRISM_CENTRAL_USERNAME}
      - PRISM_CENTRAL_PASSWORD=${PRISM_CENTRAL_PASSWORD}
    stdin_open: true
    tty: true
```

---

## Security Considerations

### Credentials

- Never commit credentials to version control
- Use environment variables or secret management
- Consider using Nutanix IAM API keys for automation

### Network

- The MCP server connects to Prism Central on port 9440 (HTTPS)
- Ensure network access between the MCP server host and Prism Central
- For production, always use `PRISM_CENTRAL_VERIFY_SSL=true`

### API Keys (Recommended for Automation)

Create a service account with API key:

```bash
# Use the IAM API to create a service account and API key
# See: https://developers.nutanix.com (IAM namespace)
```

Then configure:

```bash
PRISM_CENTRAL_HOST=192.168.1.100
PRISM_CENTRAL_API_KEY=your-api-key
```

---

## Troubleshooting

### Connection Refused

```
Error: Connection refused to 192.168.1.100:9440
```

- Verify Prism Central is accessible
- Check firewall rules
- Confirm the port is correct (default 9440)

### Authentication Failed

```
Error: 401 Unauthorized
```

- Verify username and password
- Check if the account is locked
- Ensure the user has API access permissions

### SSL Certificate Error

```
Error: SSL certificate verify failed
```

For development only:
```bash
PRISM_CENTRAL_VERIFY_SSL=false
```

For production, add the Prism Central CA certificate to your trust store.

### Rate Limiting

```
Error: 429 Too Many Requests
```

Prism Central rate limits vary by deployment size:
- X-Small: 30 req/s
- Small: 40 req/s
- Large: 60 req/s
- X-Large: 80 req/s

The server includes automatic retry with backoff.

---

## Updating

```bash
cd ntnx-mcp
git pull
uv pip install -e .
```

---

## Logs

The MCP server logs to stderr (not stdout, as per MCP protocol).

View logs:
```bash
python -m ntnx_mcp 2>ntnx-mcp.log
```

Set log level:
```bash
export LOG_LEVEL=DEBUG
python -m ntnx_mcp
```
