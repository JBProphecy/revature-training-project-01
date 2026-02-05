import pandas as pd
from pathlib import Path

def convert_to_dataframe(config):
    path = Path(config.path)

    #Check if file path exists, if not raise an error
    if not path.exists():
        raise FileNotFoundError(f"File not found: {config.path}")

    if config.format == "csv":
        df = pd.read_csv(path)
    elif config.format == "json":
        df = pd.read_json(path)
    else:
        raise ValueError(f"Unsupported data format: {config.format}")
    
    
    if config.field_map:
        df = df[list(config.field_map.keys())].rename(columns=config.field_map)
    
    return df