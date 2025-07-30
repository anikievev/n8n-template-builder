from .base import BaseNode
from typing import Optional, Dict, Any


class IfNode(BaseNode):
    """IF node for n8n workflows."""
    
    def __init__(self, name: str = "IF", parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.if", parameters)
        
    def set_conditions(self, conditions: Dict[str, Any]) -> None:
        """Set the conditions for the IF node."""
        # Convert conditions to the correct n8n format
        if "boolean" in conditions and isinstance(conditions["boolean"], dict):
            # Single condition case - wrap in array
            self.set_parameter("conditions", {
                "boolean": [conditions["boolean"]]
            })
        elif "boolean" in conditions and isinstance(conditions["boolean"], list):
            # Already in correct format
            self.set_parameter("conditions", conditions)
        else:
            # Assume it's a single condition dict, wrap it
            self.set_parameter("conditions", {
                "boolean": [conditions]
            })
        
    def set_combinator(self, combinator: str) -> None:
        """Set the combinator for multiple conditions (AND/OR)."""
        self.set_parameter("combinator", combinator)
