################################################################################################

import logging
import pandas as pd

from pandas import DataFrame
from pathlib import Path

################################################################################################

from project.models import PipelineConfigurationSettings as Config

################################################################################################

logger = logging.getLogger(__name__)

################################################################################################

class LoadExternalDataError(Exception):
  def __init__(self, reason: str = "N/A", format: str = "N/A", path: str | Path = "N/A"):
    self.message = f"load external data error :: reason = {reason} :: format = {format} :: path = {path}"
    self.reason = reason
    self.format = format
    self.path = path
    super().__init__(self.message)

################################################################################################

# config is not used right now, but it could be helpful later, like for declaring datatypes specifially
def load_external_data(config: Config, source: Config.External.Source) -> DataFrame:
  """
  ### **Throws**

  `LoadExternalDataError` - if an error occurs
  """
  logger.info("loading external data")
  logger.debug("format = %s", source.format.value)
  logger.debug("path = %s", source.path)
  try:
    match source.format:
      case Config.External.Source.Format.CSV:
        data = pd.read_csv(source.path, engine="pyarrow", dtype_backend="pyarrow")
        logger.info("external data has been loaded")
        return data
      case Config.External.Source.Format.JSON:
        data = pd.read_json(source.path, dtype_backend="pyarrow")
        logger.info("external data has been loaded")
        return data
  except FileNotFoundError as e:
    logger.warning("failed to load external data")
    exception = LoadExternalDataError(reason=f"FileNotFoundError = {type(e).__name__}", format=source.format.value, path=source.path)
    logger.error(exception.message)
    raise exception from e
  except IsADirectoryError as e:
    logger.warning("failed to load external data")
    exception = LoadExternalDataError(reason=f"IsADirectoryError = {type(e).__name__}", format=source.format.value, path=source.path)
    logger.error(exception.message)
    raise exception from e
  except PermissionError as e:
    logger.warning("failed to load external data")
    exception = LoadExternalDataError(reason=f"PermissionError = {type(e).__name__}", format=source.format.value, path=source.path)
    logger.error(exception.message)
    raise exception from e
  except OSError as e:
    logger.warning("failed to load external data")
    exception = LoadExternalDataError(reason=f"OSError = {type(e).__name__}", format=source.format.value, path=source.path)
    logger.error(exception.message)
    raise exception from e
  # We could handle some other errors that are specific to Pandas.
  except Exception as e:
    logger.warning("failed to load external data")
    exception = LoadExternalDataError(reason=f"OSError = {type(e).__name__}", format=source.format.value, path=source.path)
    logger.error(exception.message)
    raise exception from e

################################################################################################

__all__ = ["load_external_data", "LoadExternalDataError"]

################################################################################################
