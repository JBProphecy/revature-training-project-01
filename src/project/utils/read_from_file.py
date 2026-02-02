################################################################################################

import json
import logging
import yaml

from project.errors import ReadFileError

from typing import Any

################################################################################################

logger = logging.getLogger(__name__)

################################################################################################

def read_json_from_file(path: str) -> Any:
  try:
    with open(file=path, mode="r") as file: return json.load(file)
  except Exception as e:
    logger.error("Error Reading JSON from File")
    logger.debug("path = %s", path)
    raise ReadFileError("Error Reading JSON from File", path=path) from e

################################################################################################

def read_yaml_from_file(path: str) -> Any:
  try:
    with open(file=path, mode="r") as file:
      return yaml.safe_load(file)
  except Exception as e:
    logger.error("Error Reading YAML from File")
    logger.debug("path = %s", path)
    raise ReadFileError("Error Reading YAML from File", path=path) from e

################################################################################################

__all__ = [
  "read_json_from_file",
  "read_yaml_from_file"
]

################################################################################################
