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

UPDATE_BATCH_PROCESS = load_sql("update_batch_process.sql")

################################################################################################

class UpdateBatchProcessError(AbstractError): pass

################################################################################################

def update_batch_process(
  id: UUID,
  final_timestamp: datetime
):
  """
  ### **Throws**

  `UpdateBatchProcessError`
  """
  try:
    logger.debug("updating batch process %s", id)
    with dbengine.begin() as connection:
      connection.execute(UPDATE_BATCH_PROCESS, {
        "id": id,
        "final_timestamp": final_timestamp
      })
    logger.debug("batch process %s has been updated", id)
  except Exception as e:
    logger.warning("failed to updated batch process %s", id)
    exception = UpdateBatchProcessError("means = failed to update batch process", f"cause = {type(e).__name__}")
    logger.error(exception.message)
    raise exception from e

################################################################################################

__all__ = ["update_batch_process", "UpdateBatchProcessError"]

################################################################################################
