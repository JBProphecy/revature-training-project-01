from project.models import Source
from project.utils import load_config_from_file

aaa = load_config_from_file("config/tornado_usa_sources.yaml", list[Source])