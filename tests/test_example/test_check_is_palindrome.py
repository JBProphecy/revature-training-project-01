################################################################################################

import pytest

from typing import Callable

################################################################################################

from example.check_is_palindrome import (
  check_is_palindrome_perfect_match_for_loop,
  check_is_palindrome_perfect_match_while_loop
)

################################################################################################

@pytest.mark.parametrize("f", [check_is_palindrome_perfect_match_for_loop, check_is_palindrome_perfect_match_while_loop])
@pytest.mark.parametrize("s, expected", [
  ("", True),
  (" ", True),
  ("\"", True),
  ("a", True),
  ("b", True),
  ("aa", True),
  ("ab", False),
  ("ba", False),
  ("bb", True),
  ("\"\"", True),
  ("hello", False),
  ("racecar", True),
  ("Racecar", False)
])
def test_check_is_palindrom_perfect_match(f: Callable[[str], bool], s: str, expected: bool):
  assert f(s) == expected

################################################################################################
