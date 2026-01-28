<div align="center">

<img src="https://img.shields.io/badge/ð§ -CogniWork-7C3AED?style=for-the-badge&labelColor=1a1a2e" alt="CogniWork"/>

# CogniWork

### ð Open Source AI Orchestration Platform

**Stop drowning in tabs. Start orchestrating your workflow.**

[![MIT License](https://img.shields.io/badge/License-MIT-7C3AED.svg?style=flat-square)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776ab.svg?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7C3AED?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/viseyyon)

<br/>

*"I don't have a productivity problem. I have an orchestration problem."*

<br/>

[Quick Start](#-quick-start) â¢
[Features](#-features) â¢
[Examples](#-examples) â¢
[Documentation](#-documentation) â¢
[Community](#-community)

</div>

---

## ð¡ The Problem

Every developer knows the feeling:

```
ð 2:00 AM
ð 47 browser tabs open
â 4th cup of coffee
ð« Manually copy-pasting between ChatGPT, IDE, logs, and docs
```

**You're not coding. You're just frantic glue holding disjointed AI tools together.**

## â¨ The Solution

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

# Run in parallel - they work while you sleep ð´
results = await orchestra.run_parallel([
    {"agent": "CodeWriter", "task": "Implement user auth"},
    {"agent": "CodeReviewer", "task": "Review the PR"},
    {"agent": "TestWriter", "task": "Write unit tests"}
])
```

---

## â¡ Quick Start

### One-Line Install

```bash
pip install cogniwork
```

### Or Clone & Run

```bash
# Clone the repo
git clone https://github.com/viseyyon/cogniwork-trial.git
cd cogniwork-trial

# Install dependencies
pip install -e .

# Run your first agent
python -c "from cogniwork import Agent; print('ð§  CogniWork Ready!')"
```

### 30-Second Demo

```python
import asyncio
from cogniwork import Agent, Orchestrator

async def main():
    # Create an agent
    agent = Agent("MyAssistant")

    # Run a task
    result = await agent.run("Analyze this codebase")
    print(f"â {result.output}")

asyncio.run(main())
```

---

## ð¯ Features

| Feature | Description |
|---------|-------------|
| ð¤ **Multi-Agent** | Run multiple AI agents in parallel |
| ð§  **Memory** | Agents remember context across sessions |
| ð§ **Tools** | Integrate GitHub, Slack, Jira, and more |
| ð **Workflows** | Chain agents in sequences |
| ðï¸ **Multi-LLM** | OpenAI, Anthropic, Ollama, Azure |
| ð **Open Core** | MIT licensed, free forever |

---

## ð¦ What's Included

```
cogniwork/
âââ __init__.py      # Package entry point
âââ core.py          # Agent, Memory, Orchestrator
âââ tools.py         # Tool framework & registry
âââ config.py        # Configuration management
```

---

## ð Why CogniWork?

| | CogniWork | Enterprise Tools |
|---|:---:|:---:|
| **Price** | $0 FREE | $50K+/year |
| **Open Source** | â MIT | â Proprietary |
| **Self-Hosted** | â Your servers | â Their cloud |
| **Customizable** | â Full control | â Limited |
| **Lock-in** | â None | â Vendor lock |

---

## ð ï¸ Examples

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

## ð Documentation

| Resource | Link |
|----------|------|
| ð Getting Started | [docs.cogniwork.ai/start](https://docs.cogniwork.ai) |
| ð§ API Reference | [docs.cogniwork.ai/api](https://docs.cogniwork.ai) |
| ð¡ Examples | [/examples](./examples) |
| ð¥ Video Tutorial | Coming Soon |

---

## ð¤ Community

<div align="center">

[![Discord](https://img.shields.io/badge/ð¬_Discord-Join_Community-7C3AED?style=for-the-badge)](https://discord.gg/viseyyon)
[![Twitter](https://img.shields.io/badge/ð¦_Twitter-@viseyyon-1DA1F2?style=for-the-badge)](https://twitter.com/viseyyon)
[![LinkedIn](https://img.shields.io/badge/ð¼_LinkedIn-Viseyyon-0A66C2?style=for-the-badge)](https://linkedin.com/company/viseyyon)

</div>

**Need help?** â [Discord](https://discord.gg/viseyyon)
**Found a bug?** â [Open an Issue](https://github.com/viseyyon/cogniwork-trial/issues)
**Want to contribute?** â [Read CONTRIBUTING.md](CONTRIBUTING.md)

---

## â­ Star History

If CogniWork helps you, give us a â­! It helps others discover the project.

---

## ð License

MIT License - Use it for anything. Free forever.

---

<div align="center">

**Built with ð by [Viseyyon Technologies](https://viseyyon.com)**

*Transform Your Business with AI-Powered Intelligence*

<br/>

<a href="https://viseyyon.com"><img src="https://img.shields.io/badge/Viseyyon-Technologies-7C3AED?style=for-the-badge" alt="Viseyyon"/></a>

</div>
