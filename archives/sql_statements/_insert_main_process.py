from datetime import datetime
from logging import getLogger
from uuid import UUID

from project.v2.abs.errors import AbstractError
from project.v2.core.dbengine import engine
from project.v2.dbquery.helpers import load_sql_from_file

logger = getLogger(__name__)

INSERT_MAIN_PROCESS = load_sql_from_file("insert_main_process.sql")

class InsertMainProcessError(AbstractError): pass

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
    logger.debug("inserting main process", extra={ "id": id })
    with engine.begin() as connection:
      connection.execute(INSERT_MAIN_PROCESS, {
        "pipeline_name": pipeline_name,
        "id": id,
        "start_timestamp": start_timestamp
      })
    logger.debug("main process has been inserted", extra={ "id": id })
  except Exception as e:
    logger.error("failed to insert main process", extra={ "cause": type(e).__name__, "pipeline_name": pipeline_name, "id": id })
    raise InsertMainProcessError(cause=type(e).__name__) from e

__all__ = ["insert_main_process", "InsertMainProcessError"]
