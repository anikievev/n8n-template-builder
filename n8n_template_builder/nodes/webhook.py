from .base import BaseNode
from typing import Optional, Dict, Any


class WebhookNode(BaseNode):
    """Webhook node for n8n workflows."""
    
    def __init__(self, name: str = "Webhook", path: Optional[str] = None, parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.webhook", parameters)
        
        # Set default Webhook parameters
        if path:
            self.set_parameter("path", path)
            
    def set_path(self, path: str) -> None:
        """Set the path for the webhook."""
        self.set_parameter("path", path)
        
    def set_response_mode(self, response_mode: str) -> None:
        """Set the response mode for the webhook."""
        self.set_parameter("responseMode", response_mode)
        
    def set_response_data(self, response_data: str) -> None:
        """Set the response data for the webhook."""
        self.set_parameter("responseData", response_data)
