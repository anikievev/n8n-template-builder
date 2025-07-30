from n8n_template_builder import (
    Workflow, 
    StartNode, 
    HttpRequestNode, 
    TelegramNode, 
    SetNode, 
    IfNode, 
    WebhookNode, 
    DiscordNode, 
    EmailSendNode,
    GoogleSheetsNode
)


def create_advanced_workflow():
    # Create a new workflow
    workflow = Workflow("Advanced Multi-Channel Notification Workflow")
    
    # Create nodes
    start = StartNode("Start Trigger")
    webhook = WebhookNode("Webhook Trigger", path="webhook-trigger")
    http = HttpRequestNode(
        name="API Request",
        url="https://jsonplaceholder.typicode.com/posts/1"
    )
    set_node = SetNode("Process Data")
    if_node = IfNode("Check Status")
    telegram = TelegramNode(
        name="Telegram Alert",
        chat_id="123456789",
        text="New post: {{ $json.title }}"
    )
    discord = DiscordNode(
        name="Discord Notification",
        webhook_uri="https://discord.com/api/webhooks/...",
        text="New post: {{ $json.title }}"
    )
    email = EmailSendNode(
        name="Email Notification",
        to="admin@example.com",
        subject="New Post Created",
        text="A new post was created: {{ $json.title }}"
    )
    sheets = GoogleSheetsNode("Log to Sheets")
    
    # Set positions for better visualization
    start.set_position(250, 100)
    webhook.set_position(250, 200)
    http.set_position(500, 150)
    set_node.set_position(750, 150)
    if_node.set_position(1000, 150)
    telegram.set_position(1200, 100)
    discord.set_position(1200, 200)
    email.set_position(1200, 300)
    sheets.set_position(1400, 150)
    
    # Configure nodes
    http.set_parameter("method", "GET")
    
    set_node.set_fields({
        "title": "={{ $json.title }}",
        "userId": "={{ $json.userId }}",
        "status": "={{ $json.id > 50 ? 'high' : 'normal' }}"
    })
    
    if_node.set_conditions({
        "boolean": {
            "value1": "={{ $json.status }}",
            "operation": "equals",
            "value2": "high"
        }
    })
    
    sheets.set_operation("append")
    sheets.set_spreadsheet_id("1BxiMVs0XRAflZpRnAIrX4Hf7pZuDzXwJ7pLd0V2A")
    sheets.set_worksheet_id("Sheet1")
    
    # Add nodes to workflow
    workflow.add_nodes(start, webhook, http, set_node, if_node, telegram, discord, email, sheets)
    
    # Connect nodes
    workflow.connect(start, http)
    workflow.connect(webhook, http)
    workflow.connect(http, set_node)
    workflow.connect(set_node, if_node)
    workflow.connect(if_node, telegram)  # True branch
    workflow.connect(if_node, discord, source_output_index=1)  # False branch
    workflow.connect(telegram, email)
    workflow.connect(discord, email)
    workflow.connect(email, sheets)
    
    # Save to file
    workflow.save_to_file("advanced_workflow.json")
    print("Advanced workflow saved to advanced_workflow.json")
    
    # Print summary
    print(f"\nWorkflow '{workflow.name}' created with {len(workflow.nodes)} nodes and {len(workflow.connections)} connections")


if __name__ == "__main__":
    create_advanced_workflow()
