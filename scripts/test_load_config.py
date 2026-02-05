from project.models import Config
from project.utils import load_config_from_file

aaa = load_config_from_file("config/wildfire_global.yaml", Config)
print(aaa.model_dump_json(indent=2))

bbb = load_config_from_file("config/tornado_usa.yaml", Config)
