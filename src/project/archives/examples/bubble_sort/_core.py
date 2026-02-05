################################################################################################

import logging

################################################################################################

logger = logging.getLogger(__name__)

################################################################################################

def bubble_sort(n: list[int]) -> list[int]:
  """
  ### **Description**

  This function will take a list of integers `n` and modify it in place using a bubble-sort algorithm.

  ---

  ### **Parameters**

  `n` :: `list[int]` - a list of integers

  ---

  ### **Returns**

  `list[int]` - `n` sorted in order from least to greatest
  """
  logger.debug("integers = %s", n)
  total_length = len(n)
  if total_length < 2: return n
  unsorted_length = total_length
  while unsorted_length >= 2:
    logger.debug("iteration = %d/%d", total_length - unsorted_length + 1, total_length - 1)
    swapped = False
    for i in range(unsorted_length - 1):
      a_index = i
      b_index = i + 1
      a_value = n[a_index]
      b_value = n[b_index]
      logger.debug("comparing (%d, %d) and (%d, %d)", a_index, a_value, b_index, b_value)
      if a_value > b_value:
        logger.debug("swapping (%d, %d) and (%d, %d)", a_index, a_value, b_index, b_value)
        n[a_index], n[b_index] = b_value, a_value
        swapped = True
    if not swapped:
      logger.debug("nothing swapped :: early exit")
      break
    unsorted_length -= 1
  logger.debug("integers = %s", n)
  return n

################################################################################################
