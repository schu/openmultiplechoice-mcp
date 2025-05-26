# omc-mcp

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
                "</ABSOLUTE/PATH/TO/omc-mcp>",
                "run",
                "omc-mcp.py"
            ],
            "env": {
                "OMC_API_TOKEN": "<YOUR_API_TOKEN>"
            }
        }
    }
}
```