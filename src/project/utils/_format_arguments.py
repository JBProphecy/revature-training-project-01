import json
from typing import Any

def format_listed_arguments(arguments: tuple[Any, ...], sep: str = " :: ") -> str:
  return sep.join(json.dumps(item) for item in arguments)

def format_mapped_arguments(arguments: dict[str, Any], sep: str = " :: ") -> str:
  return sep.join(f"{key} = {json.dumps(value)}" for key, value in arguments.items())

def format_double_arguments(listed: tuple[Any, ...], mapped: dict[str, Any], double_sep: str = " :::: ", listed_sep: str = " :: ", mapped_sep: str = " :: ") -> str:
  return double_sep.join(filter(lambda x: x is not None, [format_listed_arguments(listed, sep=listed_sep), format_mapped_arguments(mapped, sep=mapped_sep)]))

__all__ = [
  "format_listed_arguments",
  "format_mapped_arguments",
  "format_double_arguments"
]
