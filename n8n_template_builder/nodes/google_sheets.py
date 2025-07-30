from .base import BaseNode
from typing import Optional, Dict, Any


class GoogleSheetsNode(BaseNode):
    """Google Sheets node for n8n workflows."""
    
    def __init__(self, name: str = "Google Sheets", parameters: Optional[Dict[str, Any]] = None):
        super().__init__(name, "n8n-nodes-base.googleSheets", parameters)
        
    def set_operation(self, operation: str) -> None:
        """Set the operation to perform (append, clear, delete, read, update)."""
        self.set_parameter("operation", operation)
        
    def set_spreadsheet_id(self, spreadsheet_id: str) -> None:
        """Set the Google Spreadsheet ID."""
        self.set_parameter("sheetId", spreadsheet_id)
        
    def set_worksheet_id(self, worksheet_id: str) -> None:
        """Set the Google Worksheet ID."""
        self.set_parameter("worksheetId", worksheet_id)
        
    def set_key_row(self, key_row: int) -> None:
        """Set the key row number."""
        self.set_parameter("keyRow", key_row)
        
    def set_row_number(self, row_number: int) -> None:
        """Set the row number."""
        self.set_parameter("rowNumber", row_number)
        
    def set_columns(self, columns: Dict[str, Any]) -> None:
        """Set the columns for the operation."""
        self.set_parameter("columns", columns)
