# import logging
# import pandas as pd

# from pandas import DataFrame
# from pathlib import Path

# from project.core import configure_logging
# from project.errors import AbstractError
# from project.models import Config

# logger = logging.getLogger(__name__)
# configure_logging()

# class LoadExternalDataError(AbstractError): pass

# def load_external_data(config: Config, source_index: int) -> DataFrame:
#   """
#   ### **Throws**

#   `LoadExternalDataError`
#   """
#   source = config.sources[source_index]
#   logger.info("loading external data")
#   try:
#     match source.format:
#       case Config.Source.Format.CSV:
#         data = pd.read_csv(source.path, engine="pyarrow", dtype_backend="pyarrow")
#         logger.info("external data has been loaded")
#         return data
#       case Config.Source.Format.JSON:
#         data = pd.read_json(source.path, dtype_backend="pyarrow")
#         logger.info("external data has been loaded")
#         return data
#   except Exception as e:
#     logger.error("failed to load external data :: config_path = %s :: source_index = %d :: souce_path = %s :: source_format = %s", config.path, source_index, source.path, source.format)
#     raise LoadExternalDataError("failed to load external data", error_name=type(e).__name__, source_index=source_index, source_path=source.path, source_format=source.format)

# __all__ = ["load_external_data", "LoadExternalDataError"]

import logging
from pathlib import Path

import pandas as pd
from pandas import DataFrame

from project.core import configure_logging
from project.errors import AbstractError
from project.models import Config

logger = logging.getLogger(__name__)
configure_logging()


class LoadExternalDataError(AbstractError):
    pass


def load_external_data(config: Config, source_index: int) -> DataFrame:
    """
    Loads one external source into a pandas DataFrame.

    Raises:
        LoadExternalDataError
    """
    source = config.sources[source_index]

    # Normalize format to a simple lowercase string (works for strings or Enum-like values)
    fmt = source.format
    if hasattr(fmt, "value"):  # enum-like object
        fmt = fmt.value
    fmt = str(fmt).strip().lower()

    # Resolve/normalize path (optional but nice)
    path = Path(source.path)

    logger.info("loading external data :: path=%s :: format=%s", path, fmt)

    try:
        if fmt == "csv":
            # Keep it simple and reliable first
            data = pd.read_csv(path)

        elif fmt == "json":
            data = pd.read_json(path)

        else:
            raise ValueError(f"Unsupported source format: {source.format!r}")

        logger.info("external data has been loaded :: rows=%d cols=%d", len(data), len(data.columns))
        return data

    except Exception as e:
        # This prints the REAL error + stack trace (including NameError details)
        logger.exception(
            "failed to load external data :: source_index=%d :: source_path=%s :: source_format=%s",
            source_index, source.path, source.format
        )
        raise LoadExternalDataError(
            "failed to load external data",
            error_name=type(e).__name__,
            source_index=source_index,
            source_path=source.path,
            source_format=source.format,
        ) from e


__all__ = ["load_external_data", "LoadExternalDataError"]