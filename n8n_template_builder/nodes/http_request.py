from .base import BaseNode
from typing import Optional, Dict, Any


class HttpRequestNode(BaseNode):
    """HTTP Request node for n8n workflows."""
    
    def __init__(self, name: str = "HTTP Request", url: Optional[str] = None, method: str = "GET", parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.httpRequest", parameters)
        
        # Set default HTTP request parameters
        self.set_parameter("method", method)
        if url:
            self.set_parameter("url", url)
            
    def set_url(self, url: str) -> None:
        """Set the URL for the HTTP request."""
        self.set_parameter("url", url)
        
    def set_method(self, method: str) -> None:
        """Set the HTTP method for the request."""
        self.set_parameter("method", method)
        
    def set_body(self, body: str) -> None:
        """Set the body for the HTTP request."""
        self.set_parameter("body", body)
        
    def set_headers(self, headers: Dict[str, str]) -> None:
        """Set the headers for the HTTP request."""
        self.set_parameter("headers", headers)
