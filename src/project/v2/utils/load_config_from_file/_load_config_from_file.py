import logging
import yaml

from pathlib import Path
from typing import Type, TypeVar

from project.v2.abs.errors import AbstractError

logger = logging.getLogger(__name__)

class LoadConfigFromFileError(AbstractError): pass

T = TypeVar("T")

def load_config_from_file(
  file_path: str,
  pydantic_model: Type[T]
) -> T:
  """
  ### **Description**

  This function will load the content of a configuration file, ensure that it matches the desired schema, and return the valid object.

  ---

  ### **Parameters**

  `file_path` :: `str` - the path of the configuration file (where to look)

  `file_format` :: `ValidConfigFileFormat` - the format of the configuration file (how to process)

  ---

  ### **Throws**

  `LoadConfigFromFileError`
  """
  logger.info("loading config from file")
  try:
    with open(file_path, mode="r") as file:
      content = yaml.safe_load(file)
      result = pydantic_model(**content)
      logger.info("config has been loaded from file")
      return result
  except Exception as e:
    logger.error("failed to load config from file", extra={
      "reason": "N/A",
      "instance": type(e).__name__,
      "file_path": file_path,
    })
    raise LoadConfigFromFileError(
      "failed to load config from file",
      reason="N/A",
      instance=type(e).__name__,
      file_path=file_path,
    )
  return

__all__ = ["load_config_from_file", "LoadConfigFromFileError"]
