################################################################################################

import os

################################################################################################

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

################################################################################################

load_dotenv()

################################################################################################

def get_engine() -> Engine:
  db_host = os.getenv("DB_HOST")
  db_port = os.getenv("DB_PORT")
  db_name = os.getenv("DB_NAME")
  db_username = os.getenv("DB_USERNAME")
  db_password = os.getenv("DB_PASSWORD")

  if not all([db_host, db_port, db_name, db_username, db_password]):
    raise ValueError("Missing Database Environment Configuration Values")
  
  db_url = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

  return create_engine(db_url, pool_pre_ping=True, future=True)

################################################################################################
