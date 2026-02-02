################################################################################################

from project.types import (
  InputFieldDataType,
  SourceFormat
)

from pydantic import BaseModel

from typing import List

################################################################################################

class SourceConfiguration(BaseModel):
  format: SourceFormat
  path: str

################################################################################################

class InputFieldStructure(BaseModel):
  name: str
  type: InputFieldDataType

class OutputFieldStructure(BaseModel):
  name: str

class AdjacentFieldStructure(BaseModel):
  input: InputFieldStructure
  output: OutputFieldStructure

class FieldsConfiguration(BaseModel):
  count: int
  adjacent: List[AdjacentFieldStructure]

################################################################################################

class DataConfigurationObject(BaseModel):
  sources: List[SourceConfiguration]
  fields: FieldsConfiguration

################################################################################################
