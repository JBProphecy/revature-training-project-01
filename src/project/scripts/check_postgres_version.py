################################################################################################

import logging

from project.core import (
  configure_logging,
  dbengine,
)

from sqlalchemy.exc import (
  MultipleResultsFound,
  NoResultFound,
  SQLAlchemyError
)
from sqlalchemy.sql import text

################################################################################################

logger = logging.getLogger(__name__)

################################################################################################

def check_postgres_version():
  select_version_statement = text("SELECT version();")
  with dbengine.connect() as db:
    try:
      result = db.execute(select_version_statement)
      version = result.scalar_one()
      logger.info("Postgres Version = %s", version)
    except NoResultFound:
      logger.debug("No Result Found")
      logger.debug("There should be one and only one result.")
    except MultipleResultsFound:
      logger.debug("Multiple Results Found")
      logger.debug("There should be one and only one result.")
    except SQLAlchemyError:
      logger.debug("Unknown SQL Alchemy Error")

################################################################################################

__all__ = ["check_postgres_version"]

if __name__ == "__main__":
  configure_logging()
  check_postgres_version()

################################################################################################
