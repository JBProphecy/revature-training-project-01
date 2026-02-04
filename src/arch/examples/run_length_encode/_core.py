################################################################################################

import logging

from itertools import groupby

from typing import Any, Generator

################################################################################################

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

################################################################################################

def run_length_encoding_generator(s: str, exclude_one: bool = False) -> Generator[str, Any, None]:
  """
  ### **Description**

  This function will take a string `s` and yield each segment of its run-length-encoded form.

  ---

  ### **Parameters**

  `s` :: `str` - the string to be run-length-encoded

  `exclude_one` :: `bool` = `False` - to determine whether or not `1` should be placed after a single-character segment

  ---

  ### **Yields**

  `str` - one segment of the run-length-encoded form of `s` for the current iteration

  ---

  ### **Returns**

  `Generator[str, Any, None]` - a generator object
  """
  logger.debug("input = \"%s\"", s)
  for char, group in groupby(s):
    count = sum(1 for _ in group)
    result = f"{char}{count if exclude_one is False or count > 1 else ""}"
    logger.debug("(\"%s\", %d) => \"%s\"", char, count, result)
    yield result

def perform_run_length_encoding(s: str, exclude_one: bool = False) -> str:
  """
  ### **Description**

  This function will take a string `s` and return its run-length-encoded form.

  ---

  ### **Parameters**

  `s` :: `str` - the string to be run-length-encoded

  `exclude_one` :: `bool` = `False` - to determine whether or not `1` should be placed after a single-character segment

  - `False` - `1` will be placed after a single-character segment

  - `True` - `1` will not be placed after a single-character segment

  ---

  ### **Returns**

  `str` - a run-length-encoded string
  """
  logger.debug("input = \"%s\"", s)
  result = "".join(run_length_encoding_generator(s, exclude_one=exclude_one))
  logger.debug("result = \"%s\"", result)
  return result

################################################################################################
