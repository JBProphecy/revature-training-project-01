import logging
import yaml

from pydantic import ValidationError

from project.errors import AbstractError
from project.models import Config

logger = logging.getLogger(__name__)

class LoadConfigFromFileError(AbstractError): pass

def load_config_from_yaml(path: str) -> Config:
  """
  ### **Description**

  This function will load the content of a `YAML` file into a `Config` object.

  ---

  ### **Parameters**

  `path` :: `str` - the path of the configuration file

  ---

  ### **Throws**

  `LoadConfigFromFileError`
  """
  logger.info("loading config from yaml")
  try:
    with open(path, mode="r") as file:
      content = yaml.safe_load(file)
      result = Config(**content)
      logger.info("successfully loaded config from yaml")
      return result
  except ValidationError as e:
    logger.error("failed to load config from yaml :: path = %s :: error_name = %s :: error_count = %d", path, type(e).__name__, e.error_count())
    raise LoadConfigFromFileError(message="failed to load config from yaml", path=path, error_name=type(e).__name__, error_count=e.error_count()) from e
  except Exception as e:
    logger.error("failed to load config from yaml :: path = %s", path)
    raise LoadConfigFromFileError(message="failed to load config from yaml", path=path) from e
  return

__all__ = ["load_config_from_yaml", "LoadConfigFromFileError"]
