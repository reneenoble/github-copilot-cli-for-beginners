# Building a Custom MCP Server

> ⚠️ **This content is completely optional.** You can be highly productive with Copilot CLI using only the pre-built MCP servers (GitHub, filesystem, Context7). This guide is for developers who want to connect Copilot to custom internal APIs. See the [MCP for Beginners course](https://github.com/microsoft/mcp-for-beginners) for more details.
>
> **Prerequisites:**
> - Comfortable with TypeScript
> - Experience with Node.js
> - Understanding of async/await patterns
>
> **[← Back to Chapter 06: MCP Servers](README.md)**

---

Want to connect Copilot to your own APIs? Here's how to build a simple MCP server.

## Project Setup

```bash
mkdir weather-mcp-server
cd weather-mcp-server
npm init -y
npm install @modelcontextprotocol/sdk
```

## Server Implementation

```typescript
// index.ts
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server({
  name: 'weather-server',
  version: '1.0.0'
}, {
  capabilities: {
    tools: {}
  }
});

// Define available tools
server.setRequestHandler('tools/list', async () => ({
  tools: [
    {
      name: 'get_weather',
      description: 'Get current weather for a city',
      inputSchema: {
        type: 'object',
        properties: {
          city: {
            type: 'string',
            description: 'City name'
          }
        },
        required: ['city']
      }
    }
  ]
}));

// Handle tool calls
server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;

  if (name === 'get_weather') {
    // In real implementation, call weather API
    const weather = await fetchWeather(args.city);
    return {
      content: [{
        type: 'text',
        text: `Weather in ${args.city}: ${weather.temp}F, ${weather.conditions}`
      }]
    };
  }

  throw new Error(`Unknown tool: ${name}`);
});

async function fetchWeather(city: string) {
  // Mock implementation - replace with actual API call
  return {
    temp: 72,
    conditions: 'Partly cloudy'
  };
}

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

## Configuration

Add to your `~/.copilot/mcp-config.json`:

```json
{
  "mcpServers": {
    "weather": {
      "type": "local",
      "command": "node",
      "args": ["./weather-mcp-server/index.js"],
      "tools": ["*"]
    }
  }
}
```

## Usage

```bash
copilot

> What's the weather in Seattle?

Weather in Seattle: 72F, Partly cloudy
```

## Next Steps

Once you've built a basic server, you can:

1. **Add more tools** - Each tool is a function Copilot can call
2. **Connect real APIs** - Replace mock data with actual API calls
3. **Add authentication** - Handle API keys and tokens
4. **Publish to npm** - Share your server with others

## Resources

- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk)
- [Example MCP Servers](https://github.com/modelcontextprotocol/servers)

---

**[← Back to Chapter 06: MCP Servers](README.md)**
