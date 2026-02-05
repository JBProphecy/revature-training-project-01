from pydantic import BaseModel
from project.models import AbstractStringEnum

class Source(BaseModel):
  path: str
  format: Format
  class Format(AbstractStringEnum):
    CSV = "csv"
    JSON = "json"
  columns: dict[str, str]

__all__ = ["Source"]
