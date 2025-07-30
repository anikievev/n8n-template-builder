from .base import BaseNode
from typing import Optional, Dict, Any


class EmailSendNode(BaseNode):
    """Email Send node for n8n workflows."""
    
    def __init__(self, name: str = "Email Send", to: Optional[str] = None, subject: Optional[str] = None, text: Optional[str] = None, parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.emailSend", parameters)
        
        # Set default Email Send parameters
        if to:
            self.set_parameter("to", to)
        if subject:
            self.set_parameter("subject", subject)
        if text:
            self.set_parameter("text", text)
            
    def set_to(self, to: str) -> None:
        """Set the recipient email address."""
        self.set_parameter("to", to)
        
    def set_subject(self, subject: str) -> None:
        """Set the email subject."""
        self.set_parameter("subject", subject)
        
    def set_text(self, text: str) -> None:
        """Set the email text content."""
        self.set_parameter("text", text)
        
    def set_html(self, html: str) -> None:
        """Set the email HTML content."""
        self.set_parameter("html", html)
        
    def set_cc(self, cc: str) -> None:
        """Set the CC email addresses."""
        self.set_parameter("cc", cc)
        
    def set_bcc(self, bcc: str) -> None:
        """Set the BCC email addresses."""
        self.set_parameter("bcc", bcc)
