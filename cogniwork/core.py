"""
CogniWork Core - Agent Framework and Orchestration Engine
"""

import asyncio
import uuid
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional
from datetime import datetime
from enum import Enum


class AgentStatus(Enum):
    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    WAITING = "waiting"


@dataclass
class Memory:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    data: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def store(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.updated_at = datetime.now()

    def retrieve(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def clear(self) -> None:
        self.data = {}
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "data": self.data,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Memory":
        memory = cls(id=data.get("id", str(uuid.uuid4())))
        memory.data = data.get("data", {})
        return memory


@dataclass
class AgentResult:
    success: bool
    output: Any
    error: Optional[str] = None
    execution_time: float = 0.0
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class Agent:
    def __init__(self, name: str, model: str = "gpt-4",
                 system_prompt: Optional[str] = None,
                 memory: Optional[Memory] = None,
                 max_iterations: int = 10, temperature: float = 0.7):
        self.id = str(uuid.uuid4())
        self.name = name
        self.model = model
        self.system_prompt = system_prompt or f"You are {name}, an AI agent."
        self.memory = memory or Memory()
        self.max_iterations = max_iterations
        self.temperature = temperature
        self.tools: Dict[str, Callable] = {}
        self.status = AgentStatus.IDLE

    def add_tool(self, tool) -> "Agent":
        self.tools[tool.name] = tool
        return self

    def remove_tool(self, tool_name: str) -> "Agent":
        if tool_name in self.tools:
            del self.tools[tool_name]
        return self

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        self.status = AgentStatus.RUNNING
        start_time = datetime.now()
        try:
            self.memory.store("current_task", task)
            result = await self._execute_task(task, context)
            self.status = AgentStatus.COMPLETED
            self.memory.store("last_result", result)
            return AgentResult(success=True, output=result,
                             execution_time=(datetime.now() - start_time).total_seconds(),
                             metadata={"agent_id": self.id, "agent_name": self.name})
        except Exception as e:
            self.status = AgentStatus.FAILED
            return AgentResult(success=False, output=None, error=str(e),
                             execution_time=(datetime.now() - start_time).total_seconds())

    async def _execute_task(self, task: str, context: Optional[Dict[str, Any]]) -> Any:
        await asyncio.sleep(0.1)
        return {"task": task, "status": "completed",
                "message": f"Agent {self.name} processed task successfully",
                "tools_available": list(self.tools.keys())}

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "model": self.model,
                "memory": self.memory.to_dict(), "status": self.status.value}


class Orchestrator:
    def __init__(self, name: str = "CogniWork Orchestrator"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.agents: Dict[str, Agent] = {}
        self.workflows: Dict[str, List[str]] = {}
        self.shared_memory = Memory()

    def add_agent(self, agent: Agent) -> "Orchestrator":
        self.agents[agent.name] = agent
        return self

    def remove_agent(self, agent_name: str) -> "Orchestrator":
        if agent_name in self.agents:
            del self.agents[agent_name]
        return self

    def create_workflow(self, name: str, agent_sequence: List[str]) -> "Orchestrator":
        self.workflows[name] = agent_sequence
        return self

    async def run_agent(self, agent_name: str, task: str,
                       context: Optional[Dict[str, Any]] = None) -> AgentResult:
        if agent_name not in self.agents:
            return AgentResult(success=False, output=None,
                             error=f"Agent '{agent_name}' not found")
        return await self.agents[agent_name].run(task, context)

    async def run_parallel(self, tasks: List[Dict[str, str]],
                          context: Optional[Dict[str, Any]] = None) -> List[AgentResult]:
        async def run_single(t): return await self.run_agent(t.get("agent"), t.get("task", ""), context)
        return list(await asyncio.gather(*[run_single(t) for t in tasks]))

    async def run_workflow(self, workflow_name: str, initial_task: str,
                          context: Optional[Dict[str, Any]] = None) -> List[AgentResult]:
        if workflow_name not in self.workflows:
            return [AgentResult(success=False, output=None, error=f"Workflow '{workflow_name}' not found")]
        results, ctx = [], context or {}
        for agent_name in self.workflows[workflow_name]:
            result = await self.run_agent(agent_name, initial_task, ctx)
            results.append(result)
            if result.success: ctx["previous_result"] = result.output
            else: break
        return results

    def get_status(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "total_agents": len(self.agents),
                "agents": {n: a.status.value for n, a in self.agents.items()},
                "workflows": list(self.workflows.keys())}
