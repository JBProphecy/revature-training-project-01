################################################################################################

from app import dbengine, configure_logging
from sqlalchemy import text
from sqlalchemy.exc import NoResultFound, MultipleResultsFound, SQLAlchemyError

################################################################################################

import logging

logger = logging.getLogger(__name__)

################################################################################################

configure_logging()

################################################################################################

select_version_statement = text("SELECT version();")

def get_postgres_version():
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

get_postgres_version()

################################################################################################
