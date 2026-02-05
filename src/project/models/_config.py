from pydantic import BaseModel
from project.models import Source

class Config(BaseModel):
  keyname: str
  sources: list[Source]

__all__ = ["Config"]
