from functools import lru_cache
from pathlib import Path
from sqlalchemy import text

from project.v2.core.environment import settings

@lru_cache
def load_sql_from_file(filename: str):
  path = Path(settings.sql_statements_path) / Path(filename)
  return text(path.read_text())

__all__ = ["load_sql_from_file"]
