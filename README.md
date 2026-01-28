<div align="center">

<img src="https://img.shields.io/badge/CogniWork-7C3AED?style=for-the-badge&labelColor=1a1a2e" alt="CogniWork"/>

# CogniWork

### Open Source AI Orchestration Platform

**Stop drowning in tabs. Start orchestrating your workflow.**

[![MIT License](https://img.shields.io/badge/License-MIT-7C3AED.svg?style=flat-square)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776ab.svg?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7C3AED?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/viseyyon)

<br/>

*"I don't have a productivity problem. I have an orchestration problem."*

<br/>

[Quick Start](#-quick-start) | [Features](#-features) | [Examples](#-examples) | [Docs](#-documentation) | [Community](#-community)

</div>

---

## The Problem

Every developer knows the feeling:

```
2:00 AM
47 browser tabs open
4th cup of coffee
Manually copy-pasting between ChatGPT, IDE, logs, and docs
```

**You're not coding. You're just frantic glue holding disjointed AI tools together.**

## The Solution

CogniWork orchestrates your AI agents so they work **together**, not in silos.

```python
from cogniwork import Agent, Orchestrator

# Create specialized agents
coder = Agent("CodeWriter", model="gpt-4")
reviewer = Agent("CodeReviewer", model="claude-3")
tester = Agent("TestWriter", model="gpt-4")

# Orchestrate them
orchestra = Orchestrator()
orchestra.add_agent(coder)
orchestra.add_agent(reviewer)
orchestra.add_agent(tester)

# Run in parallel - they work while you sleep
results = await orchestra.run_parallel([
    {"agent": "CodeWriter", "task": "Implement user auth"},
    {"agent": "CodeReviewer", "task": "Review the PR"},
    {"agent": "TestWriter", "task": "Write unit tests"}
])
```

---

## Quick Start

### One-Line Install

```bash
pip install cogniwork
```

### Or Clone and Run

```bash
# Clone the repo
git clone https://github.com/viseyyon/cogniwork-trial.git
cd cogniwork-trial

# Install dependencies
pip install -e .

# Run your first agent
python -c "from cogniwork import Agent; print('CogniWork Ready!')"
```

### 30-Second Demo

```python
import asyncio
from cogniwork import Agent

async def main():
    # Create an agent
    agent = Agent("MyAssistant")

    # Run a task
    result = await agent.run("Analyze this codebase")
    print(f"Done: {result.output}")

asyncio.run(main())
```

---

## Features

| Feature | Description |
|---------|-------------|
| **Multi-Agent** | Run multiple AI agents in parallel |
| **Memory** | Agents remember context across sessions |
| **Tools** | Integrate GitHub, Slack, Jira, and more |
| **Workflows** | Chain agents in sequences |
| **Multi-LLM** | OpenAI, Anthropic, Ollama, Azure |
| **Open Core** | MIT licensed, free forever |

---

## What's Included

```
cogniwork/
    __init__.py      # Package entry point
    core.py          # Agent, Memory, Orchestrator
    tools.py         # Tool framework and registry
    config.py        # Configuration management
```

---

## Why CogniWork?

| | CogniWork | Enterprise Tools |
|---|:---:|:---:|
| **Price** | $0 FREE | $50K+/year |
| **Open Source** | Yes (MIT) | No |
| **Self-Hosted** | Your servers | Their cloud |
| **Customizable** | Full control | Limited |
| **Lock-in** | None | Vendor lock |

---

## Examples

### Code Review Pipeline

```python
orchestra = Orchestrator()
orchestra.create_workflow("code_review", [
    "StaticAnalyzer",
    "SecurityScanner",
    "CodeReviewer",
    "DocumentationChecker"
])

results = await orchestra.run_workflow("code_review", "Review PR #123")
```

### Automated Bug Triage

```python
from cogniwork import Agent
from cogniwork.tools import create_shell_tool

bug_agent = Agent("BugTriager")
bug_agent.add_tool(create_shell_tool())

result = await bug_agent.run("Analyze error logs and create Jira tickets")
```

---

## Documentation

| Resource | Link |
|----------|------|
| Getting Started | [docs.cogniwork.ai](https://docs.cogniwork.ai) |
| API Reference | [docs.cogniwork.ai/api](https://docs.cogniwork.ai/api) |
| Examples | [/examples](./examples) |

---

## Community

[![Discord](https://img.shields.io/badge/Discord-Join_Community-7C3AED?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/viseyyon)
[![Twitter](https://img.shields.io/badge/Twitter-@viseyyon-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/viseyyon)

**Need help?** [Join Discord](https://discord.gg/viseyyon)

**Found a bug?** [Open an Issue](https://github.com/viseyyon/cogniwork-trial/issues)

**Want to contribute?** [Read CONTRIBUTING.md](CONTRIBUTING.md)

---

## License

MIT License - Use it for anything. Free forever.

---

<div align="center">

**Built with care by [Viseyyon Technologies](https://viseyyon.com)**

*Transform Your Business with AI-Powered Intelligence*

<br/>

<a href="https://viseyyon.com"><img src="https://img.shields.io/badge/Viseyyon-Technologies-7C3AED?style=for-the-badge" alt="Viseyyon"/></a>

</div>
