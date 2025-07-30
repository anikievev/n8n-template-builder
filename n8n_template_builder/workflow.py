from typing import Dict, Any, List, Optional
from .nodes.base import BaseNode
import json


class Workflow:
    """Main class representing an n8n workflow."""
    
    def __init__(self, name: str):
        self.name = name
        self.nodes: List[BaseNode] = []
        self.connections: List[Dict[str, Any]] = []
        
    def add_node(self, node: BaseNode) -> None:
        """Add a single node to the workflow."""
        self.nodes.append(node)
        
    def add_nodes(self, *nodes: BaseNode) -> None:
        """Add multiple nodes to the workflow."""
        for node in nodes:
            self.add_node(node)
            
    def connect(self, source_node: BaseNode, target_node: BaseNode, source_output_index: int = 0, target_input_index: int = 0) -> None:
        """Create a connection between two nodes."""
        connection = {
            "sourceId": source_node.id,
            "targetId": target_node.id,
            "sourceOutputIndex": source_output_index,
            "targetInputIndex": target_input_index
        }
        self.connections.append(connection)
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert the workflow to a dictionary representation."""
        nodes_dict = [node.to_dict() for node in self.nodes]
        
        # Convert connections to n8n format (object with node names as keys)
        connections_dict = {}
        for connection in self.connections:
            source_node = self.get_node_by_id(connection["sourceId"])
            target_node = self.get_node_by_id(connection["targetId"])
            
            if source_node and target_node:
                source_name = source_node.name
                target_name = target_node.name
                
                # Create the connection structure expected by n8n
                if source_name not in connections_dict:
                    connections_dict[source_name] = {}
                
                # For main output (index 0), use "main" key
                output_type = "main"
                output_index = connection["sourceOutputIndex"]
                
                if output_type not in connections_dict[source_name]:
                    connections_dict[source_name][output_type] = [None] * (output_index + 1)
                
                # Extend the array if needed
                if len(connections_dict[source_name][output_type]) <= output_index:
                    connections_dict[source_name][output_type].extend([None] * (output_index - len(connections_dict[source_name][output_type]) + 1))
                
                # Create the connection object
                connection_obj = {
                    "node": target_name,
                    "type": "main",
                    "index": connection["targetInputIndex"]
                }
                
                # For multiple connections from the same output, use an array
                if connections_dict[source_name][output_type][output_index] is None:
                    connections_dict[source_name][output_type][output_index] = [connection_obj]
                else:
                    connections_dict[source_name][output_type][output_index].append(connection_obj)
        
        return {
            "name": self.name,
            "nodes": nodes_dict,
            "connections": connections_dict,
            "active": False,
            "settings": {
                "executionOrder": "v1"
            },
            "versionId": "placeholder_version_id"
        }
        
    def save_to_file(self, filename: str) -> None:
        """Save the workflow to a JSON file."""
        workflow_dict = self.to_dict()
        with open(filename, 'w') as f:
            json.dump(workflow_dict, f, indent=2)
            
    def get_node_by_id(self, node_id: str) -> Optional[BaseNode]:
        """Get a node by its ID."""
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None
