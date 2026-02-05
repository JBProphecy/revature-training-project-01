from project.utils import load_config_from_yaml
from project.sandbox.load_external_data import load_external_data

CONFIG_FILE_PATH = "config/wildfire_global.yaml"
config = load_config_from_yaml(CONFIG_FILE_PATH)
print(config.model_dump_json(indent=2))
config.path = CONFIG_FILE_PATH
load_external_data(config, 0)

# df = load_external_data(bbb, 0)