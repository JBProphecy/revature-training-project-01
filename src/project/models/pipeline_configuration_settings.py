################################################################################################

from enum import Enum
from pydantic import BaseModel
from typing import Dict, List

################################################################################################

class PipelineConfigurationSettings(BaseModel):
  name: str
  internal: Internal
  external: External

  class Internal(BaseModel):
    table: Table

    class Table(BaseModel):
      fields: Fields

      class Fields(BaseModel):
        list: List[str]

  class External(BaseModel):
    sources: List[Source]

    class Source(BaseModel):
      format: Format
      path: str
      table: Table

      class Format(str, Enum):
        CSV = "CSV"
        JSON = "JSON"

      class Table(BaseModel):
        fields: Fields

        class Fields(BaseModel):
          map: Dict[str, str]

################################################################################################

__all__ = ["PipelineConfigurationSettings"]

################################################################################################
