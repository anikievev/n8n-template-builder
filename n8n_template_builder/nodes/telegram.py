from .base import BaseNode
from typing import Optional, Dict, Any


class TelegramNode(BaseNode):
    """Telegram node for n8n workflows."""
    
    def __init__(self, name: str = "Telegram", chat_id: Optional[str] = None, text: Optional[str] = None, parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.telegram", parameters)
        
        # Set default Telegram parameters
        if chat_id:
            self.set_parameter("chatId", chat_id)
        if text:
            self.set_parameter("text", text)
            
    def set_chat_id(self, chat_id: str) -> None:
        """Set the chat ID for the Telegram message."""
        self.set_parameter("chatId", chat_id)
        
    def set_text(self, text: str) -> None:
        """Set the text for the Telegram message."""
        self.set_parameter("text", text)
        
    def set_additional_fields(self, fields: Dict[str, Any]) -> None:
        """Set additional fields for the Telegram message."""
        self.set_parameter("additionalFields", fields)
