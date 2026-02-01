################################################################################################

import logging

from app import dbengine
from tests import configure_logging
from pytest import fixture
from sqlalchemy.exc import SQLAlchemyError

################################################################################################

configure_logging()

logger = logging.getLogger(__name__)

################################################################################################

@fixture
def connection():
  try:
    logger.info("Establishing Database Connection")
    with dbengine.connect() as connection:
      logger.info("Database Connection Established")
      yield connection
  except SQLAlchemyError:
    logger.error("SQLAlchemyError: Failed to Establish Database Connection")
    raise
  except:
    logger.error("Unknown Error: Failed to Establish Database")
  finally:
    logger.info("Database Connection Fixture Destroyed")

################################################################################################
