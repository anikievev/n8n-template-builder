from .base import BaseNode
from typing import Optional, Dict, Any


class DiscordNode(BaseNode):
    """Discord node for n8n workflows."""
    
    def __init__(self, name: str = "Discord", webhook_uri: Optional[str] = None, text: Optional[str] = None, parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.discord", parameters)
        
        # Set default Discord parameters
        if webhook_uri:
            self.set_parameter("webhookUri", webhook_uri)
        if text:
            self.set_parameter("text", text)
            
    def set_webhook_uri(self, webhook_uri: str) -> None:
        """Set the webhook URI for the Discord message."""
        self.set_parameter("webhookUri", webhook_uri)
        
    def set_text(self, text: str) -> None:
        """Set the text for the Discord message."""
        self.set_parameter("text", text)
        
    def set_embed(self, embed: Dict[str, Any]) -> None:
        """Set the embed for the Discord message."""
        self.set_parameter("embed", embed)
