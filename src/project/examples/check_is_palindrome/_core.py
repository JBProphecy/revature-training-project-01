################################################################################################

import logging

################################################################################################

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

################################################################################################

def check_is_palindrome_perfect_match_for_loop(s: str) -> bool:
  """
  ### **Description**

  This function will take a string `s` and determine whether or not it's a palindrome.

  ---

  ### **Parameters**

  `s` :: `str` - a string

  ---

  ### **Returns**

  `bool` - `True` if `s` is a palindrome

  `bool` - `False` if `s` is not a palindrome
  """
  logger.debug("string = \"%s\"", s)
  length = len(s)
  for i in range(length // 2):
    left_index = i
    right_index = length - 1 - i
    left_value = s[left_index]
    right_value = s[right_index]
    logger.debug("comparing (%d, \"%s\") and (%d, \"%s\")", left_index, left_value, right_index, right_value)
    if left_value != right_value:
      logger.debug("\"%s\" is not a palindrome", s)
      return False
  logger.debug("\"%s\" is a palindrome", s)
  return True

################################################################################################

def check_is_palindrome_perfect_match_while_loop(s: str) -> bool:
  """
  ### **Description**

  This function will take a string `s` and determine whether or not it's a palindrome.

  ---

  ### **Parameters**

  `s` :: `str` - a string

  ---

  ### **Returns**

  `bool` - `True` if `s` is a palindrome

  `bool` - `False` if `s` is not a palindrome
  """
  logger.debug("string = \"%s\"", s)
  left_index = 0
  right_index = len(s) - 1
  while left_index < right_index:
    left_value = s[left_index]
    right_value = s[right_index]
    logger.debug("comparing (%d, \"%s\") and (%d, \"%s\")", left_index, left_value, right_index, right_value)
    if left_value != right_value:
      logger.debug("\"%s\" is not a palindrome", s)
      return False
    left_index += 1
    right_index -= 1
  logger.debug("\"%s\" is a palindrome", s)
  return True

################################################################################################
