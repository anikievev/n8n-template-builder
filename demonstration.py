#!/usr/bin/env python3
"""
Demonstration script for n8n-template-builder library.

This script showcases the capabilities of the n8n-template-builder library
by creating various example workflows that demonstrate different features
and node types.
"""

import json
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


def demo_simple_workflow():
    """Create a simple workflow with just a few nodes."""
    print("=== Simple Workflow Demo ===")
    
    # Create workflow
    workflow = Workflow("Simple Demo Workflow")
    
    # Create nodes
    start = StartNode()
    http = HttpRequestNode(url="https://jsonplaceholder.typicode.com/posts/1")
    telegram = TelegramNode(chat_id="123456789", text="New post: {{ $json.title }}")
    
    # Add nodes to workflow
    workflow.add_nodes(start, http, telegram)
    
    # Connect nodes
    workflow.connect(start, http)
    workflow.connect(http, telegram)
    
    # Save to file
    workflow.save_to_file("demo_simple_workflow.json")
    print(f"Simple workflow created with {len(workflow.nodes)} nodes and {len(workflow.connections)} connections")
    return workflow


def demo_advanced_workflow():
    """Create an advanced workflow with multiple node types and branches."""
    print("\n=== Advanced Workflow Demo ===")
    
    # Create workflow
    workflow = Workflow("Advanced Demo Workflow")
    
    # Create nodes
    start = StartNode("Start Trigger")
    webhook = WebhookNode("Webhook Trigger", path="demo-webhook")
    http = HttpRequestNode(
        name="API Request",
        url="https://jsonplaceholder.typicode.com/posts"
    )
    set_node = SetNode("Process Data")
    if_node = IfNode("Check Status")
    telegram = TelegramNode(
        name="Telegram Alert",
        chat_id="123456789",
        text="High priority post: {{ $json.title }}"
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
    workflow.save_to_file("demo_advanced_workflow.json")
    print(f"Advanced workflow created with {len(workflow.nodes)} nodes and {len(workflow.connections)} connections")
    return workflow


def demo_workflow_with_custom_parameters():
    """Create a workflow with custom parameters and credentials."""
    print("\n=== Custom Parameters Demo ===")
    
    # Create workflow
    workflow = Workflow("Custom Parameters Workflow")
    
    # Create nodes
    start = StartNode("Custom Start")
    http = HttpRequestNode(
        name="Authenticated API Request",
        url="https://api.example.com/data"
    )
    
    # Set custom parameters
    http.set_parameter("method", "POST")
    http.set_parameter("ignoreSSLErrors", True)
    http.set_parameter("responseFormat", "json")
    
    # Set headers
    http.set_headers({
        "Content-Type": "application/json",
        "Authorization": "Bearer {{ $credential.apiKey }}"
    })
    
    # Set credentials
    http.set_credential("httpBasicAuth", "my-credentials")
    
    # Add nodes to workflow
    workflow.add_nodes(start, http)
    workflow.connect(start, http)
    
    # Save to file
    workflow.save_to_file("demo_custom_parameters.json")
    print(f"Custom parameters workflow created with {len(workflow.nodes)} nodes and {len(workflow.connections)} connections")
    return workflow


def main():
    """Run all demonstrations."""
    print("n8n-template-builder Library Demonstration")
    print("=" * 45)
    
    # Run demonstrations
    demo_simple_workflow()
    demo_advanced_workflow()
    demo_workflow_with_custom_parameters()
    
    print("\nDemonstration complete!")
    print("Generated workflow files:")
    print("- demo_simple_workflow.json")
    print("- demo_advanced_workflow.json")
    print("- demo_custom_parameters.json")


if __name__ == "__main__":
    main()
