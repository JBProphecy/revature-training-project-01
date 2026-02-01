################################################################################################

from app.core._env import settings
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

################################################################################################

def build_engine() -> Engine:
  host = settings.db_host
  port = settings.db_port
  name = settings.db_name
  username = settings.db_username
  password = settings.db_password
  url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{name}"
  return create_engine(url, pool_pre_ping=True, future=True)

################################################################################################

engine = build_engine()

################################################################################################
