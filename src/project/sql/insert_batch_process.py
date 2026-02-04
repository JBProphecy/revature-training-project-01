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

INSERT_BATCH_PROCESS = load_sql("insert_batch_process.sql")

################################################################################################

class InsertBatchProcessError(AbstractError): pass

################################################################################################

def insert_batch_process(
  main_process_id: UUID,
  id: UUID,
  source_index: int,
  source_path: str,
  start_timestamp: datetime
):
  """
  ### **Throws**

  `InsertBatchProcessError`
  """
  try:
    logger.debug("inserting batch process %s", id)
    with dbengine.begin() as connection:
      connection.execute(INSERT_BATCH_PROCESS, {
        "main_process_id": main_process_id,
        "id": id,
        "source_index": source_index,
        "source_path": source_path,
        "start_timestamp": start_timestamp
      })
    logger.debug("batch process %s has been inserted", id)
  except Exception as e:
    logger.warning("failed to insert batch process %s", id)
    exception = InsertBatchProcessError("means = failed to insert batch process", f"cause = {type(e).__name__}")
    logger.error(exception.message)
    raise exception from e

################################################################################################

__all__ = ["insert_batch_process", "InsertBatchProcessError"]

################################################################################################
