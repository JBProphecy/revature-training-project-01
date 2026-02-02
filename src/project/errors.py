################################################################################################

from typing import Any

################################################################################################

class NameValueError(Exception):
  def __init__(self, message: str, name: str | None = None, value: Any | None = None):
    self.message = message
    self.name = name
    self.value = value
    super().__init__(message)
  def __str__(self):
    return self.message

class PropertyError(NameValueError):
  def __init__(self, message: str, name: str | None = None, value: Any | None = None):
    super().__init__(message, name, value)

class ParseError(NameValueError):
  def __init__(self, message: str, name: str | None = None, value: Any | None = None):
    super().__init__(message, name, value)

class ReadFileError(Exception):
  def __init__(self, message: str, path: str | None = None):
    self.message = message
    self.path = path
    super().__init__(message)
  def __str__(self): return self.message

class ReturnError(NameValueError):
  def __init__(self, message: str, name: str | None = None, value: Any | None = None):
    super().__init__(message, name, value)

class ListError(NameValueError):
  def __init__(self, message: str, name: str | None = None, value: Any | None = None, index: int | None = None):
    super().__init__(message, name, value)

################################################################################################
