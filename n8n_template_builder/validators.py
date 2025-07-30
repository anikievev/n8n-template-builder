from typing import Dict, Any, List
from .nodes.base import BaseNode


def validate_node_parameters(node: BaseNode) -> Dict[str, Any]:
    """Validate node parameters based on node type.
    
    Args:
        node (BaseNode): The node to validate
        
    Returns:
        Dict[str, Any]: Validation results with 'valid' boolean and 'errors' list
    """
    errors = []
    
    # Validate based on node type
    if node.type == "n8n-nodes-base.httpRequest":
        if "url" not in node.parameters:
            errors.append("HTTP Request node requires a 'url' parameter")
        if "method" in node.parameters and node.parameters["method"] not in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
            errors.append("HTTP Request method must be one of: GET, POST, PUT, DELETE, PATCH")
    
    elif node.type == "n8n-nodes-base.telegram":
        if "chatId" not in node.parameters:
            errors.append("Telegram node requires a 'chatId' parameter")
        if "text" not in node.parameters:
            errors.append("Telegram node requires a 'text' parameter")
    
    elif node.type == "n8n-nodes-base.start":
        # Start node typically doesn't require parameters
        pass
    
    # Add validation for other node types as needed
    
    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


def validate_workflow(workflow_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a workflow dictionary.
    
    Args:
        workflow_dict (Dict[str, Any]): The workflow dictionary to validate
        
    Returns:
        Dict[str, Any]: Validation results with 'valid' boolean and 'errors' list
    """
    errors = []
    
    # Check required fields
    required_fields = ["name", "nodes", "connections"]
    for field in required_fields:
        if field not in workflow_dict:
            errors.append(f"Workflow missing required field: {field}")
    
    # Validate nodes
    if "nodes" in workflow_dict:
        node_ids = [node["id"] for node in workflow_dict["nodes"]]
        
        # Check for duplicate node IDs
        if len(node_ids) != len(set(node_ids)):
            errors.append("Workflow contains duplicate node IDs")
        
        # Validate each node
        for node in workflow_dict["nodes"]:
            # Check required node fields
            required_node_fields = ["id", "name", "type", "position"]
            for field in required_node_fields:
                if field not in node:
                    errors.append(f"Node {node.get('name', 'unknown')} missing required field: {field}")
    
    # Validate connections
    if "connections" in workflow_dict:
        # New connection format is an object with node names as keys
        if isinstance(workflow_dict["connections"], dict):
            # For now, we'll just check that it's a dict, more detailed validation can be added later
            pass
        else:
            # Old format - array of connections
            for connection in workflow_dict["connections"]:
                required_connection_fields = ["sourceId", "targetId"]
                for field in required_connection_fields:
                    if field not in connection:
                        errors.append(f"Connection missing required field: {field}")
                
                # Check if source and target nodes exist
                if "sourceId" in connection and connection["sourceId"] not in node_ids:
                    errors.append(f"Connection sourceId {connection['sourceId']} does not exist")
                if "targetId" in connection and connection["targetId"] not in node_ids:
                    errors.append(f"Connection targetId {connection['targetId']} does not exist")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
