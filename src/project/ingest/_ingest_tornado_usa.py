from project.utils import load_config_from_yaml, load_external_data

CONFIG_FILE_PATH = "config/tornado_usa.yaml"

def ingest_tornado_usa():
  config = load_config_from_yaml(CONFIG_FILE_PATH)
  config.path = CONFIG_FILE_PATH
  for i in range(len(config.sources)):
    source = config.sources[i]
    df = load_external_data(config, i)
    df = df[list(source.columns.keys())].rename(columns=source.columns)
    print(df)

__all__ = ["ingest_tornado_usa"]