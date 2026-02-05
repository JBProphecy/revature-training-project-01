import logging

from sqlalchemy import inspect
from sqlalchemy.exc import MultipleResultsFound, NoResultFound, SQLAlchemyError
from sqlalchemy.sql import text

from project.v2.core.dbengine import engine
from project.v2.logging import configure as configure_logging

logger = logging.getLogger(__name__)
inspector = inspect(engine)

def check_table_names():
  select_version_statement = text("SELECT version();")
  with engine.connect() as db:
    try:
      result = db.execute(select_version_statement)
      version = result.scalar_one()
      logger.info("Postgres Version = %s", version)
      print(inspector.get_table_names(schema="public"))
    except NoResultFound:
      logger.debug("No Result Found")
      logger.debug("There should be one and only one result.")
    except MultipleResultsFound:
      logger.debug("Multiple Results Found")
      logger.debug("There should be one and only one result.")
    except SQLAlchemyError as e:
      print(e)
      logger.debug("Unknown SQL Alchemy Error")

__all__ = ["check_table_names"]

if __name__ == "__main__":
  configure_logging()
  check_table_names()
