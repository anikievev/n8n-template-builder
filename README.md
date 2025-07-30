# n8n-template-builder

A Python library for programmatically creating n8n workflow JSON templates.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Components](#core-components)
- [Supported Node Types](#supported-node-types)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

`n8n-template-builder` is a Python library designed to generate valid JSON templates for n8n workflows programmatically. It enables developers to create, connect, and export workflows containing built-in (base) nodes without relying on the n8n UI.

This library provides an object-oriented interface to construct workflows using Python, supporting all base (official) n8n nodes and enabling users to programmatically define:
- Node types and configuration
- Connections between nodes
- Positions (layout)
- Export to a .json file compatible with n8n import

## Features

- Object-oriented interface to construct workflows using Python
- Support for base n8n nodes (Start, HTTP Request, Telegram, etc.)
- Programmatic definition of:
  - Node types and configuration
  - Connections between nodes
  - Positions (layout)
- Export to JSON file compatible with n8n import
- Built-in validation of node configurations
- Custom parameter setting for nodes
- Credential management
- Multiple connection outputs (for IF nodes, etc.)
- Position setting for visual layout
- Node-specific convenience methods

## Installation

```bash
pip install n8n-template-builder
```

Or for development:

```bash
git clone https://github.com/your-username/n8n-template-builder.git
cd n8n-template-builder
pip install -e .
```

## Quick Start

### Basic Example

```python
from n8n_template_builder import Workflow, StartNode, HttpRequestNode, TelegramNode

# Create a new workflow
workflow = Workflow("My Workflow")

# Create nodes
start = StartNode()
http = HttpRequestNode(url="https://example.com/api")
telegram = TelegramNode(chat_id="123", text="{{ $json.result }}")

# Add nodes to workflow
workflow.add_nodes(start, http, telegram)

# Connect nodes
workflow.connect(start, http)
workflow.connect(http, telegram)

# Save to file
workflow.save_to_file("my_workflow.json")
```

### Advanced Example

```python
from n8n_template_builder import (
    Workflow, 
    StartNode, 
    HttpRequestNode, 
    TelegramNode, 
    SetNode, 
    IfNode, 
    WebhookNode
)

# Create a new workflow
workflow = Workflow("Advanced Workflow")

# Create nodes with custom names and parameters
start = StartNode("Start Trigger")
http = HttpRequestNode(
    name="API Request",
    url="https://jsonplaceholder.typicode.com/posts",
    method="POST"
)
telegram = TelegramNode(
    name="Notify Admin",
    chat_id="123456789",
    text="New post created: {{ $json.title }}"
)

# Set positions for better visualization
start.set_position(250, 300)
http.set_position(500, 300)
telegram.set_position(750, 300)

# Add custom parameters
http.set_parameter("ignoreSSLErrors", True)
http.set_headers({"Content-Type": "application/json"})
telegram.set_additional_fields({"disable_notification": True})

# Add nodes to workflow
workflow.add_nodes(start, http, telegram)

# Connect nodes
workflow.connect(start, http)
workflow.connect(http, telegram)

# Save to file
workflow.save_to_file("advanced_workflow.json")
```

## Core Components

### Workflow Class

The main class representing an n8n workflow.

#### Methods
- `Workflow(name)` - Create a new workflow with the given name
- `add_node(node)` - Add a single node to the workflow
- `add_nodes(*nodes)` - Add multiple nodes to the workflow
- `connect(source_node, target_node, source_output_index=0, target_input_index=0)` - Connect two nodes
- `save_to_file(filename)` - Save the workflow to a JSON file
- `to_dict()` - Convert the workflow to a dictionary representation
- `get_node_by_id(node_id)` - Get a node by its ID

### BaseNode Class

Abstract base class for all node types.

#### Methods
- `set_position(x, y)` - Set the node's position in the workflow editor
- `set_parameter(key, value)` - Set a single parameter
- `set_parameters(dict)` - Set multiple parameters at once
- `set_credential(type, name)` - Set credentials for the node
- `to_dict()` - Convert the node to a dictionary representation

### Specialized Node Classes

Each specialized node class provides convenience methods for setting common parameters.

#### HttpRequestNode
- `set_url(url)` - Set the request URL
- `set_method(method)` - Set the HTTP method
- `set_body(body)` - Set the request body
- `set_headers(headers)` - Set request headers

#### TelegramNode
- `set_chat_id(chat_id)` - Set the chat ID
- `set_text(text)` - Set the message text
- `set_additional_fields(fields)` - Set additional message fields

#### SetNode
- `set_fields(fields)` - Set the fields to set
- `set_keep_only_set(keep_only_set)` - Set whether to keep only set fields

#### IfNode
- `set_conditions(conditions)` - Set the conditions for the IF node
- `set_combinator(combinator)` - Set the combinator for multiple conditions (AND/OR)

#### WebhookNode
- `set_path(path)` - Set the path for the webhook
- `set_response_mode(response_mode)` - Set the response mode for the webhook
- `set_response_data(response_data)` - Set the response data for the webhook

#### DiscordNode
- `set_webhook_uri(webhook_uri)` - Set the webhook URI for the Discord message
- `set_text(text)` - Set the text for the Discord message
- `set_embed(embed)` - Set the embed for the Discord message

#### EmailSendNode
- `set_to(to)` - Set the recipient email address
- `set_subject(subject)` - Set the email subject
- `set_text(text)` - Set the email text content
- `set_html(html)` - Set the email HTML content
- `set_cc(cc)` - Set the CC email addresses
- `set_bcc(bcc)` - Set the BCC email addresses

#### GoogleSheetsNode
- `set_operation(operation)` - Set the operation to perform (append, clear, delete, read, update)
- `set_spreadsheet_id(spreadsheet_id)` - Set the Google Spreadsheet ID
- `set_worksheet_id(worksheet_id)` - Set the Google Worksheet ID
- `set_key_row(key_row)` - Set the key row number
- `set_row_number(row_number)` - Set the row number
- `set_columns(columns)` - Set the columns for the operation

## Supported Node Types

The library includes specialized classes for common n8n node types:

### Core Nodes
- `StartNode` - Start node (`n8n-nodes-base.start`)
- `SetNode` - Set node (`n8n-nodes-base.set`)
- `IfNode` - IF node (`n8n-nodes-base.if`)
- `WebhookNode` - Webhook node (`n8n-nodes-base.webhook`)

### HTTP & API Nodes
- `HttpRequestNode` - HTTP Request node (`n8n-nodes-base.httpRequest`)

### Messaging & Notification
- `TelegramNode` - Telegram node (`n8n-nodes-base.telegram`)
- `DiscordNode` - Discord node (`n8n-nodes-base.discord`)
- `EmailSendNode` - Email Send node (`n8n-nodes-base.emailSend`)

### Storage
- `GoogleSheetsNode` - Google Sheets node (`n8n-nodes-base.googleSheets`)

### All Supported Base Modules

#### Core Nodes
Node Type | n8n Type Name
---|---
Start | n8n-nodes-base.start
Set | n8n-nodes-base.set
IF | n8n-nodes-base.if
Switch | n8n-nodes-base.switch
Merge | n8n-nodes-base.merge
Wait | n8n-nodes-base.wait
NoOp | n8n-nodes-base.noOp
Code (JavaScript) | n8n-nodes-base.code
Function (old) | n8n-nodes-base.function
Function Item | n8n-nodes-base.functionItem
Execute Command | n8n-nodes-base.executeCommand
Webhook | n8n-nodes-base.webhook

#### HTTP & API Nodes
Node Type | n8n Type Name
---|---
HTTP Request | n8n-nodes-base.httpRequest
Webhook | n8n-nodes-base.webhook

#### Messaging & Notification
Node Type | n8n Type Name
---|---
Telegram | n8n-nodes-base.telegram
Discord | n8n-nodes-base.discord
Slack | n8n-nodes-base.slack
Email (Send) | n8n-nodes-base.emailSend
Email (Read IMAP) | n8n-nodes-base.emailReadImap

#### Storage
Node Type | n8n Type Name
---|---
Google Sheets | n8n-nodes-base.googleSheets
Notion | n8n-nodes-base.notion
Airtable | n8n-nodes-base.airtable
PostgreSQL | n8n-nodes-base.postgres
MySQL | n8n-nodes-base.mySql

#### Authentication & Identity
Node Type | n8n Type Name
---|---
HTTP Request with Auth | n8n-nodes-base.httpRequest
OAuth2 Helpers | Handled via credentials, not a node

#### AI & NLP
Node Type | n8n Type Name
---|---
OpenAI | n8n-nodes-base.openAi

## Examples

The library includes several example scripts:

### Basic Example (`example_workflow.py`)
- Simple 3-node workflow (Start → HTTP Request → Telegram)
- Demonstrates basic usage

### Advanced Example (`advanced_example.py`)
- Complex 9-node workflow with multiple branches
- Demonstrates all major node types
- Shows conditional branching with IF node

### Demonstration (`demonstration.py`)
- Multiple examples showing different features
- Custom parameters and credentials
- Position management

Run any example with:
```bash
python example_workflow.py
```

This will generate an `example_workflow.json` file that can be imported into n8n.

## Testing

The library includes a comprehensive test suite to verify functionality:

```bash
python test_library.py
```

### Test Suite (`test_library.py`)
- Basic workflow creation test
- Advanced workflow creation test
- Workflow export test
- All tests passing

## Project Structure

```
n8n_template_builder/
├── workflow.py          # Workflow class
├── __init__.py          # Package exports
├── utils.py             # Utility functions
├── validators.py
