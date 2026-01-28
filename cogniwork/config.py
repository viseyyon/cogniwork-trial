"""CogniWork Configuration Management."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional
import json
import os

@dataclass
class LLMConfig:
    """LLM provider configuration."""
    provider: str = "anthropic"
    model: str = "claude-sonnet-4-20250514"
    api_key: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 4096
    
    def __post_init__(self):
        if not self.api_key:
            self.api_key = os.getenv(f"{self.provider.upper()}_API_KEY")

@dataclass
class TelemetryConfig:
    """Telemetry and logging configuration."""
    enabled: bool = True
    log_level: str = "INFO"
    log_file: Optional[str] = None
    metrics_enabled: bool = False
    trace_enabled: bool = False

@dataclass
class MemoryConfig:
    """Memory system configuration."""
    backend: str = "local"
    max_items: int = 1000
    ttl_seconds: int = 3600
    persistence_path: Optional[str] = None

@dataclass
class Config:
    """Main configuration container."""
    llm: LLMConfig = field(default_factory=LLMConfig)
    telemetry: TelemetryConfig = field(default_factory=TelemetryConfig)
    memory: MemoryConfig = field(default_factory=MemoryConfig)
    custom: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def load(cls, path: str | Path) -> Config:
        """Load configuration from JSON file."""
        path = Path(path)
        if not path.exists():
            return cls()
        with open(path) as f:
            data = json.load(f)
        return cls(
            llm=LLMConfig(**data.get("llm", {})),
            telemetry=TelemetryConfig(**data.get("telemetry", {})),
            memory=MemoryConfig(**data.get("memory", {})),
            custom=data.get("custom", {})
        )
    
    def save(self, path: str | Path) -> None:
        """Save configuration to JSON file."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "llm": {k: v for k, v in self.llm.__dict__.items() if v is not None},
            "telemetry": self.telemetry.__dict__,
            "memory": {k: v for k, v in self.memory.__dict__.items() if v is not None},
            "custom": self.custom
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get custom configuration value."""
        return self.custom.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set custom configuration value."""
        self.custom[key] = value

def get_default_config() -> Config:
    """Get default configuration, loading from standard paths if available."""
    paths = [Path("cogniwork.json"), Path.home() / ".cogniwork" / "config.json"]
    for p in paths:
        if p.exists():
            return Config.load(p)
    return Config()
