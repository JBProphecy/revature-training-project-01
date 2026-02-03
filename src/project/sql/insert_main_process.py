################################################################################################

from datetime import datetime
from logging import getLogger
from uuid import UUID

################################################################################################

from project.core import dbengine
from project.errors import AbstractError
from project.utils import load_sql

################################################################################################

logger = getLogger(__name__)

################################################################################################

INSERT_MAIN_PROCESS = load_sql("insert_main_process.sql")

################################################################################################

class InsertMainProcessError(AbstractError): pass

################################################################################################

def insert_main_process(
  pipeline_name: str,
  id: UUID,
  start_timestamp: datetime
):
  """
  ### **Throws**

  `InsertMainProcessError`
  """
  try:
    logger.debug("inserting main process %s", id)
    with dbengine.begin() as connection:
      connection.execute(INSERT_MAIN_PROCESS, {
        "pipeline_name": pipeline_name,
        "id": id,
        "start_timestamp": start_timestamp
      })
    logger.debug("main process %s has been inserted", id)
  except Exception as e:
    logger.warning("failed to insert main process %s", id)
    exception = InsertMainProcessError("means = failed to insert main process", f"cause = {type(e).__name__}")
    logger.error(exception.message)
    raise exception from e

################################################################################################

__all__ = ["insert_main_process", "InsertMainProcessError"]

################################################################################################
