from n8n_template_builder import Workflow, StartNode, HttpRequestNode, TelegramNode


def create_example_workflow():
    # Create a new workflow
    workflow = Workflow("My Example Workflow")
    
    # Create nodes
    start = StartNode()
    http = HttpRequestNode(url="https://jsonplaceholder.typicode.com/posts/1")
    telegram = TelegramNode(chat_id="123456789", text="New post: {{ $json.title }}")
    
    # Set positions for better visualization
    start.set_position(250, 300)
    http.set_position(500, 300)
    telegram.set_position(750, 300)
    
    # Add nodes to workflow
    workflow.add_nodes(start, http, telegram)
    
    # Connect nodes
    workflow.connect(start, http)
    workflow.connect(http, telegram)
    
    # Save to file
    workflow.save_to_file("example_workflow.json")
    print("Workflow saved to example_workflow.json")
    
    # Print the workflow JSON
    import json
    workflow_dict = workflow.to_dict()
    print("\nGenerated workflow JSON:")
    print(json.dumps(workflow_dict, indent=2))


if __name__ == "__main__":
    create_example_workflow()
