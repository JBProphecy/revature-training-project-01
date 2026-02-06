################################################################################################

import logging

################################################################################################

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

################################################################################################

def multiply_digits(n: int) -> int:
  """
  ### **Description**

  This function will take an integer `n` and then...
  - `a` - throw `ValueError` if `n < 0`
  - `b` - return `n` if `n < 10`
  - `c` - return the product of `1` and each digit from `n` if `n >= 10`

  ---

  ### **Parameters**

  `n` :: `int` - any integer (should be a non-negative integer)

  ---

  ### **Returns**

  `int` - `n` if `n < 10`

  `int` - the product of `1` and each digit from `n` if `n >= 10`

  ---

  ### **Throws**

  `ValueError` if `n < 0`
  """
  logger.debug("n = %d", n)
  if n < 0: raise ValueError(f"non-negative integer required :: n = {n}")
  if n < 10: return n
  product = 1
  while n > 0:
    product *= n % 10
    n //= 10
  logger.debug("product = %d", product)
  return product

################################################################################################

def multiply_digits_until_single_loop(n: int) -> int:
  """
  ### **Description**

  This function will take an integer `n` and then...
  - `a` - throw `ValueError` if `n < 0`
  - `b` - return `n` if `n < 10`
  - `c` - compute the product of `1` and each digit from `n` and then repeat steps `b` and `c` where `n = new product`

  ---

  ### **Parameters**

  `n` :: `int` - an integer (should be a non-negative integer)

  ---

  ### **Returns**

  `int` - a single-digit integer

  ---

  ### **Throws**

  `ValueError` if `n < 0`
  """
  logger.debug("n = %d", n)
  if n < 0: raise ValueError(f"non-negative integer required :: n = {n}")
  if n < 10: return n
  while n >= 10: n = multiply_digits(n)
  return n

################################################################################################

def multiply_digits_until_single_recursive(n: int) -> int:
  """
  ### **Description**

  This function will take an integer `n` and then...
  - `a` - throw `ValueError` if `n < 0`
  - `b` - return `n` if `n < 10`
  - `c` - compute the product of `1` and each digit from `n` and then return the result of calling this function with the new product

  ---

  ### **Parameters**

  `n` :: `int` - an integer (should be a non-negative integer)

  ---

  ### **Returns**

  `int` - a single-digit integer

  ---

  ### **Throws**

  `ValueError` if `n < 0`
  """
  logger.debug("n = %d", n)
  if n < 0: raise ValueError(f"non-negative integer required :: n = {n}")
  if n < 10: return n
  return multiply_digits_until_single_recursive(multiply_digits(n))

################################################################################################
