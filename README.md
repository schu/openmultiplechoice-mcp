# openmultiplechoice-mcp

Status: experimental, work in progress

An experimental [MCP](https://modelcontextprotocol.io) server for [OpenMultipleChoice](https://github.com/openmultiplechoice/openmultiplechoice).

## Configuration

### Claude Desktop

Example `~/Library/Application\ Support/Claude/claude_desktop_config.json`:

```
{
    "mcpServers": {
        "omc": {
            "command": "uv",
            "args": [
                "--directory",
                "</ABSOLUTE/PATH/TO/openmultiplechoice-mcp>",
                "run",
                "omc-mcp.py"
            ],
            "env": {
                "OMC_API_TOKEN": "<YOUR_OMC_API_TOKEN>"
            }
        }
    }
}
```

Restart Claude Desktop for changes to take effect.
