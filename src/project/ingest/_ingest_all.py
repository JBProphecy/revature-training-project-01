
from ._ingest_tornado_usa import *
from ._ingest_wildfire_global import *

def ingest_all():
  ingest_tornado_usa()
  ingest_wildfire_global()

if __name__ == "__main__":
  ingest_all()
