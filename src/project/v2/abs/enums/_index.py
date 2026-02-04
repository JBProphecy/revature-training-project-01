from enum import Enum
from typing import Any, Tuple

class AbstractEnum(Enum):
  @classmethod
  def get_values(cls) -> Tuple[Any, ...]:
    return tuple(x.value for x in cls)

class AbstractStringEnum(str, AbstractEnum):
  @classmethod
  def get_values(cls) -> Tuple[str, ...]:
    return tuple(x.value for x in cls)

__all__ = ["AbstractEnum", "AbstractStringEnum"]
