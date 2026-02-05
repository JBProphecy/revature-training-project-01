from project.utils import load_config_from_yaml, load_external_data

CONFIG_FILE_PATH = "config/wildfire_global.yaml"

def ingest_wildfire_global():
  config = load_config_from_yaml(CONFIG_FILE_PATH)
  config.path = CONFIG_FILE_PATH
  for i in range(len(config.sources)):
    source = config.sources[i]
    df = load_external_data(config, i)
    df = df[list(source.columns.keys())].rename(columns=source.columns)
    print(df)

__all__ = ["ingest_wildfire_global"]
