from .base import BaseNode
from typing import Optional, Dict, Any


class StartNode(BaseNode):
    """Start node for n8n workflows."""
    
    def __init__(self, name: str = "Start", parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.start", parameters)
