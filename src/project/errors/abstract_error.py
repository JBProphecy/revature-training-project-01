################################################################################################

from typing import Any

################################################################################################

def format_value(value: Any) -> str:
  if isinstance(value, str): return f'"{value}"'
  return str(value)

################################################################################################

class AbstractError(Exception):
  def __init__(self, *args: Any, **kwargs):
    self.arguments = args
    self.kwargs = kwargs
    self.message = " :: ".join(
      [self.__class__.__name__] +
      [format_value(arg) for arg in args] +
      [f"{key} = {format_value(value)}" for key, value in kwargs.items()]
    )
    super().__init__(self.message)

################################################################################################

__all__ = ["AbstractError"]

################################################################################################
