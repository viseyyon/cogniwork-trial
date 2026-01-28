"""CogniWork Tool Framework for integrations."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional
import json

class ToolCategory(Enum):
    """Categories for organizing tools."""
    FILE_SYSTEM = "file_system"
    WEB = "web"
    DATABASE = "database"
    API = "api"
    CUSTOM = "custom"

@dataclass
class ToolParameter:
    """Definition of a tool parameter."""
    name: str
    type: str
    description: str
    required: bool = True
    default: Any = None

@dataclass
class ToolResult:
    """Result from tool execution."""
    success: bool
    data: Any = None
    error: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {"success": self.success, "data": self.data, "error": self.error, "metadata": self.metadata}

@dataclass
class Tool:
    """Base tool definition."""
    name: str
    description: str
    category: ToolCategory
    parameters: List[ToolParameter] = field(default_factory=list)
    handler: Optional[Callable[..., ToolResult]] = None
    enabled: bool = True
    
    def execute(self, **kwargs) -> ToolResult:
        if not self.enabled:
            return ToolResult(success=False, error=f"Tool '{self.name}' is disabled")
        if not self.handler:
            return ToolResult(success=False, error=f"No handler for tool '{self.name}'")
        try:
            for param in self.parameters:
                if param.required and param.name not in kwargs:
                    return ToolResult(success=False, error=f"Missing required parameter: {param.name}")
            return self.handler(**kwargs)
        except Exception as e:
            return ToolResult(success=False, error=str(e))
    
    def to_schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "parameters": {p.name: {"type": p.type, "description": p.description, "required": p.required} for p in self.parameters}
        }

class ToolRegistry:
    """Registry for managing tools."""
    
    def __init__(self):
        self._tools: Dict[str, Tool] = {}
    
    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool
    
    def unregister(self, name: str) -> bool:
        return self._tools.pop(name, None) is not None
    
    def get(self, name: str) -> Optional[Tool]:
        return self._tools.get(name)
    
    def list_tools(self, category: Optional[ToolCategory] = None) -> List[Tool]:
        tools = list(self._tools.values())
        return [t for t in tools if t.category == category] if category else tools
    
    def execute(self, name: str, **kwargs) -> ToolResult:
        tool = self.get(name)
        if not tool:
            return ToolResult(success=False, error=f"Tool '{name}' not found")
        return tool.execute(**kwargs)
    
    def export_schemas(self) -> List[Dict[str, Any]]:
        return [t.to_schema() for t in self._tools.values()]

def tool(name: str, description: str, category: ToolCategory = ToolCategory.CUSTOM, parameters: List[ToolParameter] = None):
    """Decorator to create a tool from a function."""
    def decorator(func: Callable[..., ToolResult]) -> Tool:
        return Tool(name=name, description=description, category=category, parameters=parameters or [], handler=func)
    return decorator
