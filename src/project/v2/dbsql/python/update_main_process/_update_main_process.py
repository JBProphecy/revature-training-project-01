from datetime import datetime
from logging import getLogger
from uuid import UUID

from project.v2.abs.errors import AbstractError
from project.v2.core.dbengine import engine
from project.v2.dbsql.helpers import load_sql_from_file

logger = getLogger(__name__)

UPDATE_MAIN_PROCESS = load_sql_from_file("update_main_process.sql")

class UpdateMainProcessError(AbstractError): pass

def update_main_process(
  id: UUID,
  final_timestamp: datetime
):
  """
  ### **Throws**

  `UpdateMainProcessError`
  """
  try:
    logger.debug("updating main process", extra={ "id": id })
    with engine.begin() as connection:
      connection.execute(UPDATE_MAIN_PROCESS, {
        "id": id,
        "final_timestamp": final_timestamp
      })
    logger.debug("main process has been updated", extra={ "id": id })
  except Exception as e:
    logger.error("failed to update main process", extra={ "cause": type(e).__name__ })
    raise UpdateMainProcessError(cause=type(e).__name__) from e

__all__ = ["update_main_process", "UpdateMainProcessError"]
