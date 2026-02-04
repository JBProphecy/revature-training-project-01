from datetime import datetime
from logging import getLogger
from uuid import UUID

from project.v2.abs.errors import AbstractError
from project.v2.core.dbengine import engine
from project.v2.dbsql.helpers import load_sql_from_file

logger = getLogger(__name__)

UPDATE_BATCH_PROCESS = load_sql_from_file("update_batch_process.sql")

class UpdateBatchProcessError(AbstractError): pass

def update_batch_process(
  id: UUID,
  final_timestamp: datetime
):
  """
  ### **Throws**

  `UpdateBatchProcessError`
  """
  try:
    logger.debug("updating batch process %s", extra={ "id": id })
    with engine.begin() as connection:
      connection.execute(UPDATE_BATCH_PROCESS, {
        "id": id,
        "final_timestamp": final_timestamp
      })
    logger.debug("batch process has been updated", extra={ "id": id })
  except Exception as e:
    logger.error("failed to update batch process", extra={ "cause": type(e).__name__ })
    raise UpdateBatchProcessError(cause=type(e).__name__) from e

__all__ = ["update_batch_process", "UpdateBatchProcessError"]
