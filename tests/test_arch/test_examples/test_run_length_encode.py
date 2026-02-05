################################################################################################

import pytest

################################################################################################

from project.examples.run_length_encode import (
  perform_run_length_encoding
)

################################################################################################

@pytest.mark.parametrize("s, expected", [
  ("hello world", "h1e1l2o1 1w1o1r1l1d1"),
  ("aaabbc", "a3b2c1"),
  ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "a37")
])
def test_perform_run_length_encoding_include_one(s: str, expected: str):
  assert perform_run_length_encoding(s, exclude_one=False) == expected

################################################################################################

@pytest.mark.parametrize("s, expected", [
  ("hello world", "hel2o world"),
  ("aaabbc", "a3b2c"),
  ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "a37")
])
def test_perform_run_length_encoding_exclude_one(s: str, expected: str):
  assert perform_run_length_encoding(s, exclude_one=True) == expected

################################################################################################
