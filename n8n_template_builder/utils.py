import json
from typing import Dict, Any


def format_json(obj: Dict[str, Any], indent: int = 2) -> str:
    """Format a dictionary as a JSON string with specified indentation."""
    return json.dumps(obj, indent=indent)


def validate_node_type(node_type: str) -> bool:
    """Validate if a node type is supported.
    
    Args:
        node_type (str): The node type to validate
        
    Returns:
        bool: True if the node type is supported, False otherwise
    """
    # List of supported base node types
    supported_types = [
        "n8n-nodes-base.start",
        "n8n-nodes-base.set",
        "n8n-nodes-base.if",
        "n8n-nodes-base.switch",
        "n8n-nodes-base.merge",
        "n8n-nodes-base.wait",
        "n8n-nodes-base.noOp",
        "n8n-nodes-base.code",
        "n8n-nodes-base.function",
        "n8n-nodes-base.functionItem",
        "n8n-nodes-base.executeCommand",
        "n8n-nodes-base.webhook",
        "n8n-nodes-base.httpRequest",
        "n8n-nodes-base.telegram",
        "n8n-nodes-base.discord",
        "n8n-nodes-base.slack",
        "n8n-nodes-base.emailSend",
        "n8n-nodes-base.emailReadImap",
        "n8n-nodes-base.googleSheets",
        "n8n-nodes-base.notion",
        "n8n-nodes-base.airtable",
        "n8n-nodes-base.postgres",
        "n8n-nodes-base.mySql",
        "n8n-nodes-base.openAi"
    ]
    
    return node_type in supported_types


def generate_node_name(node_type: str, count: int = 1) -> str:
    """Generate a default node name based on the node type.
    
    Args:
        node_type (str): The type of the node
        count (int): A counter to make names unique
        
    Returns:
        str: A generated node name
    """
    # Extract the simple name from the full type
    if "." in node_type:
        simple_name = node_type.split(".")[-1]
        # Capitalize first letter
        simple_name = simple_name[0].upper() + simple_name[1:]
    else:
        simple_name = node_type
    
    if count > 1:
        return f"{simple_name} {count}"
    return simple_name
