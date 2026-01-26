################################################################################################

from src.db import get_engine
from sqlalchemy import text

################################################################################################

def test_connection():
  engine = get_engine()
  with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))
    print(f"Postgres Version is {result.fetchone()}")

################################################################################################

if __name__ == "__main__":
  test_connection()

################################################################################################
