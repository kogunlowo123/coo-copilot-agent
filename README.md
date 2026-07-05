# COO Copilot Agent

[![CI](https://github.com/kogunlowo123/coo-copilot-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/coo-copilot-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Executive | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

COO copilot agent that monitors operational efficiency, tracks process improvement initiatives, analyzes operational costs, manages cross-functional projects, and provides operational excellence insights.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `monitor_operations` | Monitor operational efficiency metrics across departments |
| `track_process_improvements` | Track process improvement initiatives and savings |
| `analyze_operational_costs` | Analyze operational costs and identify optimization opportunities |
| `manage_cross_functional` | Manage cross-functional project status and dependencies |
| `generate_ops_report` | Generate operational excellence report with benchmarks |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/coo-copilot/synthesize` | Synthesize data |
| `POST` | `/api/v1/coo-copilot/analyze` | Analyze |
| `GET` | `/api/v1/coo-copilot/track` | Track metrics |
| `POST` | `/api/v1/coo-copilot/recommend` | Get recommendation |
| `POST` | `/api/v1/coo-copilot/report` | Generate report |

## Features

- Coo
- Copilot
- Strategic Insights
- Decision Support

## Integrations

- Snowflake
- Tableau
- Salesforce
- Workday
- Jira

## Architecture

```
coo-copilot-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── coo_copilot_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Enterprise Data Platform + LLM + BI**

---

Built as part of the Enterprise AI Agent Platform.
