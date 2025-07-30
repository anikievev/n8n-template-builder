import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from n8n_template_builder import (
    Workflow, 
    StartNode, 
    HttpRequestNode, 
    TelegramNode,
    SetNode,
    IfNode,
    WebhookNode
)
from n8n_template_builder.validators import validate_workflow, validate_node_parameters


def test_basic_workflow():
    """Test creating a basic workflow with the library."""
    print("Testing basic workflow creation...")
    
    # Create workflow
    workflow = Workflow("Test Workflow")
    
    # Create nodes
    start = StartNode()
    http = HttpRequestNode(url="https://example.com/api")
    telegram = TelegramNode(chat_id="123", text="{{ $json.result }}")
    
    # Add nodes
    workflow.add_nodes(start, http, telegram)
    
    # Connect nodes
    workflow.connect(start, http)
    workflow.connect(http, telegram)
    
    # Convert to dict
    workflow_dict = workflow.to_dict()
    
    # Validate workflow
    validation_result = validate_workflow(workflow_dict)
    assert validation_result["valid"], f"Workflow validation failed: {validation_result['errors']}"
    
    # Validate nodes
    for node in workflow.nodes:
        node_validation = validate_node_parameters(node)
        assert node_validation["valid"], f"Node {node.name} validation failed: {node_validation['errors']}"
    
    print("✓ Basic workflow test passed")
    return workflow_dict


def test_advanced_workflow():
    """Test creating an advanced workflow with the library."""
    print("Testing advanced workflow creation...")
    
    # Create workflow
    workflow = Workflow("Advanced Test Workflow")
    
    # Create nodes
    start = StartNode("Start Trigger")
    webhook = WebhookNode("Webhook Trigger", path="test-path")
    http = HttpRequestNode(name="API Request", url="https://example.com/api")
    set_node = SetNode("Process Data")
    if_node = IfNode("Check Condition")
    telegram = TelegramNode(name="Telegram Alert", chat_id="123", text="Test message")
    
    # Configure nodes
    http.set_parameter("method", "POST")
    set_node.set_fields({"processed": "={{ $json.data }}"})
    if_node.set_conditions({
        "boolean": {
            "value1": "={{ $json.status }}",
            "operation": "equals",
            "value2": "success"
        }
    })
    
    # Add nodes
    workflow.add_nodes(start, webhook, http, set_node, if_node, telegram)
    
    # Connect nodes
    workflow.connect(start, http)
    workflow.connect(webhook, http)
    workflow.connect(http, set_node)
    workflow.connect(set_node, if_node)
    workflow.connect(if_node, telegram)  # True branch
    workflow.connect(if_node, telegram, source_output_index=1)  # False branch
    
    # Convert to dict
    workflow_dict = workflow.to_dict()
    
    # Validate workflow
    validation_result = validate_workflow(workflow_dict)
    assert validation_result["valid"], f"Advanced workflow validation failed: {validation_result['errors']}"
    
    print("✓ Advanced workflow test passed")
    return workflow_dict


def test_workflow_export():
    """Test exporting workflow to JSON file."""
    print("Testing workflow export...")
    
    # Create workflow
    workflow = Workflow("Export Test Workflow")
    
    # Create and add nodes
    start = StartNode()
    http = HttpRequestNode(url="https://example.com/test")
    workflow.add_nodes(start, http)
    workflow.connect(start, http)
    
    # Export to file
    test_file = "test_export.json"
    workflow.save_to_file(test_file)
    
    # Check if file exists
    assert os.path.exists(test_file), "Export file was not created"
    
    # Check file content
    with open(test_file, 'r') as f:
        data = json.load(f)
    
    assert data["name"] == "Export Test Workflow", "Workflow name mismatch"
    assert len(data["nodes"]) == 2, "Node count mismatch"
    assert len(data["connections"]) == 1, "Connection count mismatch"
    
    # Clean up
    os.remove(test_file)
    
    print("✓ Workflow export test passed")


def main():
    """Run all tests."""
    print("Running n8n-template-builder tests...\n")
    
    try:
        # Run tests
        test_basic_workflow()
        test_advanced_workflow()
        test_workflow_export()
        
        print("\n✓ All tests passed!")
        return True
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
