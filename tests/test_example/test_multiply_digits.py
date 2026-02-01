################################################################################################

import pytest

from typing import Callable

################################################################################################

from example.multiply_digits import (
  multiply_digits,
  multiply_digits_until_single_loop,
  multiply_digits_until_single_recursive
)

################################################################################################

@pytest.mark.parametrize("f", [multiply_digits, multiply_digits_until_single_loop, multiply_digits_until_single_recursive])
@pytest.mark.parametrize("n", [-1, -6, -22, -48, -99, -237, -999999])
def test_negative_integers(f: Callable[[int], int], n: int):
  with pytest.raises(ValueError):
    f(n)

################################################################################################

@pytest.mark.parametrize("n, expected", [
  # single-digit integers
  (-0, 0),
  (0, 0),
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5),
  (6, 6),
  (7, 7),
  (8, 8),
  (9, 9),
  # double-digit-integers
  (10, 0),
  (12, 2),
  (27, 14),
  (40, 0),
  (56, 30),
  (88, 64),
  (99, 81),
  # triple-digit integers
  (123, 6),
  (286, 96),
  (999, 729)
])
def test_multiply_digits_non_negative_integers(n: int, expected: int):
  assert multiply_digits(n) == expected

################################################################################################

@pytest.mark.parametrize("f", [multiply_digits_until_single_loop, multiply_digits_until_single_recursive])
@pytest.mark.parametrize("n, expected", [
  # single-digit integers
  (0, 0),
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5),
  (6, 6),
  (7, 7),
  (8, 8),
  (9, 9),
  # double-digit-integers
  (25, 0),
  (36, 8),
  (47, 6),
  (68, 6),
  # triple-digit-integers
  (255, 0),
  (127, 4),
  (737, 6)
])
def test_multiply_digits_until_single_non_negative_integers(f: Callable[[int], int], n: int, expected: int):
  assert f(n) == expected

################################################################################################
