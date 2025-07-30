from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
import uuid


class BaseNode(ABC):
    """Base class for all n8n nodes."""
    
    def __init__(self, name: str, type_name: str, parameters: Optional[Dict[str, Any]] = None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = type_name
        self.position = [0, 0]  # [x, y] coordinates
        self.parameters = parameters or {}
        self.credentials = {}
        
    def set_position(self, x: int, y: int) -> None:
        """Set the position of the node in the workflow editor."""
        self.position = [x, y]
        
    def set_parameter(self, key: str, value: Any) -> None:
        """Set a parameter for the node."""
        self.parameters[key] = value
        
    def set_parameters(self, parameters: Dict[str, Any]) -> None:
        """Set multiple parameters for the node."""
        self.parameters.update(parameters)
        
    def set_credential(self, credential_type: str, credential_name: str) -> None:
        """Set credentials for the node."""
        self.credentials[credential_type] = credential_name
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert the node to a dictionary representation."""
        node_dict = {
            "parameters": self.parameters,
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "typeVersion": 1,
            "position": self.position
        }
        
        if self.credentials:
            node_dict["credentials"] = self.credentials
            
        return node_dict
