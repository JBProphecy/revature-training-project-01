################################################################################################

import logging

from pytest import fixture

from app.core.db import get_engine
from tests.core.logging import initialize
from sqlalchemy.exc import SQLAlchemyError

################################################################################################

initialize()

logger = logging.getLogger(__name__)

################################################################################################

@fixture
def db_conn():
  engine = get_engine()
  try:
    logger.info("Establishing Database Connection")
    with engine.connect() as conn:
      logger.info("Database Connection Established")
      yield conn
  except SQLAlchemyError as error:
    logger.error("Failed to Establish Database Connection")
    raise
  finally:
    logger.info("Database Connection Fixture Destroyed")

################################################################################################
