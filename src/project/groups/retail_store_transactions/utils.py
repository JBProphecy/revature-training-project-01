################################################################################################

from datetime import datetime, timezone
from uuid import UUID, uuid4

################################################################################################

def generate_id() -> UUID:
  return uuid4()

def generate_timestamp() -> datetime:
  return datetime.now(timezone.utc)

################################################################################################
