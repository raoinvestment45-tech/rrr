#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Clone and install TradingView MCP Jackson if not present
if [ ! -d /root/tradingview-mcp-jackson ]; then
  git clone https://github.com/LewisWJackson/tradingview-mcp-jackson.git /root/tradingview-mcp-jackson
  cd /root/tradingview-mcp-jackson && npm install
fi

# Clone and install tradingview-mcp if not present
if [ ! -d /root/tradingview-mcp ]; then
  git clone https://github.com/tradesdontlie/tradingview-mcp.git /root/tradingview-mcp
  cd /root/tradingview-mcp && npm install
fi
