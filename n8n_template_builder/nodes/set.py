from .base import BaseNode
from typing import Optional, Dict, Any


class SetNode(BaseNode):
    """Set node for n8n workflows."""
    
    def __init__(self, name: str = "Set", parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.set", parameters)
        
    def set_fields(self, fields: Dict[str, Any]) -> None:
        """Set the fields for the Set node."""
        # Convert fields dict to array format expected by n8n
        fields_array = []
        for key, value in fields.items():
            fields_array.append({
                "name": key,
                "value": value
            })
        self.set_parameter("options", {"fields": fields_array})
        
    def set_keep_only_set(self, keep_only_set: bool) -> None:
        """Set whether to keep only the set fields."""
        self.set_parameter("keepOnlySet", keep_only_set)
