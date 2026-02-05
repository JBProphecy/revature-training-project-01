from project.utils import format_double_arguments

class AbstractError(Exception):
  def __init__(self, *args, **kwargs):
    self.listed_arguments = args
    self.mapped_arguments = kwargs
    self.message = format_double_arguments(args, kwargs)
    super().__init__(self.message)

__all__ = ["AbstractError"]
