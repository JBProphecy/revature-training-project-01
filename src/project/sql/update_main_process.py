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

UPDATE_MAIN_PROCESS = load_sql("update_main_process.sql")

################################################################################################

class UpdateMainProcessError(AbstractError): pass

################################################################################################

def update_main_process(
  id: UUID,
  final_timestamp: datetime
):
  """
  ### **Throws**

  `UpdateMainProcessError`
  """
  try:
    logger.debug("updating main process %s", id)
    with dbengine.begin() as connection:
      connection.execute(UPDATE_MAIN_PROCESS, {
        "id": id,
        "final_timestamp": final_timestamp
      })
    logger.debug("main process %s has been updated", id)
  except Exception as e:
    logger.warning("failed to update main process %s", id)
    exception = UpdateMainProcessError("means = failed to update main process", f"cause = {type(e).__name__}")
    logger.error(exception.message)
    raise exception from e

################################################################################################

__all__ = ["update_main_process", "UpdateMainProcessError"]

################################################################################################
