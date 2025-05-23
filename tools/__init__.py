from typing import Dict, Type, List
from langchain.tools import BaseTool

# Tool registry implementation
_TOOL_REGISTRY: Dict[str, Type[BaseTool]] = {}

def register_tool(cls: Type[BaseTool]) -> Type[BaseTool]:
    """Decorator to register tool classes"""
    _TOOL_REGISTRY[cls.__name__] = cls
    return cls

def get_tool(name: str) -> BaseTool:
    """Get an instance of a registered tool by name"""
    if name not in _TOOL_REGISTRY:
        raise ValueError(f"Tool '{name}' not found in registry")
    return _TOOL_REGISTRY[name]()

def custom_tools() -> List[BaseTool]:
    """Get all registered tools as instances"""
    return [tool_class() for tool_class in _TOOL_REGISTRY.values()]

# Import and register tools
try:
    from tools.report_tools import ReportGenerationTool
    # The @register_tool decorator in report_tools.py will handle registration
except ImportError as e:
    raise ImportError("Failed to import tools: {e}") from e

# Clean exports
__all__ = [
    'register_tool',
    'get_tool',
    'custom_tools',
    'ReportGenerationTool'
]