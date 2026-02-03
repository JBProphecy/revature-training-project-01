################################################################################################

from pathlib import Path
from typing import Any

################################################################################################

class InvalidFieldValueError(Exception):
  def __init__(self, reason: str, field_name: str = "N/A", field_value: Any = "N/A"):
    self.message = f"invalid field value error :: reason = {reason} :: field_name = {field_name} :: field_value = {field_value}"
    self.reason = reason
    self.field_name = field_name
    self.field_value = field_value
    super().__init__(self.message)

################################################################################################

class UnknownFieldError(Exception):
  def __init__(self, reason: str = "N/A", field_name: str = "N/A", source_path: str | Path = "N/A"):
    self.message = f"unknown field error :: reason = {reason} :: field_name = {field_name} :: source_path = {source_path}"
    self.field_name = field_name
    self.source_path = source_path
    super().__init__(self.message)

################################################################################################
