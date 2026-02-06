from datetime import datetime
from logging import getLogger
from uuid import UUID

from project.v2.abs.errors import AbstractError
from project.v2.core.dbengine import engine
from project.v2.dbquery.helpers import load_sql_from_file

logger = getLogger(__name__)

INSERT_BATCH_PROCESS = load_sql_from_file("insert_batch_process.sql")

class InsertBatchProcessError(AbstractError): pass

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
    logger.debug("inserting batch process", extra={ "id": id })
    with engine.begin() as connection:
      connection.execute(INSERT_BATCH_PROCESS, {
        "main_process_id": main_process_id,
        "id": id,
        "source_index": source_index,
        "source_path": source_path,
        "start_timestamp": start_timestamp
      })
    logger.debug("batch process has been inserted", extra={ "id": id })
  except Exception as e:
    logger.error("failed to insert batch process", extra={ "cause": type(e).__name__, "main_process_id": main_process_id, "id": id, "source_index": source_index, "source_path": source_path })
    raise InsertBatchProcessError(cause=type(e).__name__) from e

__all__ = ["insert_batch_process", "InsertBatchProcessError"]
