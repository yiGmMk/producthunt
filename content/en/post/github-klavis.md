---
title: klavis
date: 2025-10-14T15:37:15+08:00
draft: False
image: https://images.unsplash.com/photo-1606655316666-327f837ba10a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjA0MjczNjh8&ixlib=rb-4.1.0
tags: ['github',Klavis AI, Strata, MCP Integrations]
categories: ['github']
---

## Quick Start

### Option 1: Cloud-hosted

Get instant access without any setup:

- Sign Up - [Create account →](https://www.klavis.ai/auth/sign-up)
- Get Started - [Follow quickstart guide →](https://docs.klavis.ai/documentation/quickstart)

### Option 2: Open Source

Self-host everything on your own infrastructure:

```bash
# Run any MCP Integration
docker pull ghcr.io/klavis-ai/github-mcp-server:latest
docker run -p 5000:5000 ghcr.io/klavis-ai/github-mcp-server:latest

# Install Open Source Strata locally
pipx install strata-mcp
strata add --type stdio playwright npx @playwright/mcp@latest
```

### Option 3: SDK

```python
# Python SDK
from klavis import Klavis
from klavis.types import McpServerName

klavis = Klavis(api_key="your-key")

# Create Strata instance
strata = klavis_client.mcp_server.create_strata_server(
    user_id="user123",
    servers=[McpServerName.GMAIL, McpServerName.SLACK],
)

# Or use individual MCP servers
gmail = klavis.mcp_server.create_server_instance(
    server_name=McpServerName.GMAIL,
    user_id="user123",
)
```

```typescript
// TypeScript SDK
import { KlavisClient, McpServerName } from 'klavis';

const klavis = new KlavisClient({ apiKey: 'your-api-key' });

// Create Strata instance
const strata = await klavis.mcpServer.createStrataServer({
    userId: "user123",
    servers: [Klavis.McpServerName.Gmail, Klavis.McpServerName.Slack],
});

// Or use individual MCP servers
const gmail = await klavis.mcpServer.createServerInstance({
    serverName: McpServerName.GMAIL,
    userId: "user123"
});
```

### Option 4: REST API


```bash
# Create Strata server
curl -X POST "https://api.klavis.ai/v1/mcp-server/strata" \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "servers": ["GMAIL", "SLACK"]
  }'

# Create individual MCP server
curl -X POST "https://api.klavis.ai/v1/mcp-server/instance" \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "server_name": "GMAIL",
    "user_id": "user123"
  }'
```


## Resources

- 📖 [Documentation](https://docs.klavis.ai)
- 💬 [Discord Community](https://discord.gg/p7TuTEcssn)
- 🐛 [Report Issues](https://github.com/klavis-ai/klavis/issues)
- 🌐 [Klavis AI Website](https://www.klavis.ai)

---

<div align="center">
  <p><strong>Made with ❤️ by the Klavis Team</strong></p>
</div>