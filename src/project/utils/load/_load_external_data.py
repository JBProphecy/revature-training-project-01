import logging
import pandas as pd

from pandas import DataFrame

from project.core import configure_logging
from project.errors import AbstractError
from project.models import Config

logger = logging.getLogger(__name__)
configure_logging()

class LoadExternalDataError(AbstractError): pass

def load_external_data(config: Config, source_index: int) -> DataFrame:
  """
  ### **Throws**

  `LoadExternalDataError`
  """
  source = config.sources[source_index]
  logger.info("loading external data")
  try:
    match source.format:
      case Config.Source.Format.CSV:
        data = pd.read_csv(source.path, engine="pyarrow", dtype_backend="pyarrow")
        logger.info("external data has been loaded")
        return data
      case Config.Source.Format.JSON:
        data = pd.read_json(source.path, dtype_backend="pyarrow")
        logger.info("external data has been loaded")
        return data
  except Exception as e:
    logger.error("failed to load external data :: config_path = %s :: source_index = %d :: souce_path = %s :: source_format = %s", config.path, source_index, source.path, source.format)
    raise LoadExternalDataError("failed to load external data", error_name=type(e).__name__, source_index=source_index, source_path=source.path, source_format=source.format)

__all__ = ["load_external_data", "LoadExternalDataError"]
