from project.cleaning._clean_wildfire import clean_wildfire
from project.cleaning._clean_tornado import clean_tornado_usa

from project.validation._validate_wildfire import validate_wildfire
from project.validation._validate_tornado_usa import validate_tornado_usa

from project.dedupe._dedupe_wildfire import dedupe_wildfire
from project.dedupe._dedupe_tornado import dedupe_tornado


PIPELINES = {
    "wildfire": {
        "clean": clean_wildfire,
        "dedupe": dedupe_wildfire,
        "validate": validate_wildfire,
        "accepted_table": "wildfire_global",
        "rejects_table": "wildfire_global_rejects",
    },
    "tornado": {
        "clean": clean_tornado_usa,
        "dedupe": dedupe_tornado,
        "validate": validate_tornado_usa,
        "accepted_table": "tornado_usa",
        "rejects_table": "tornado_usa_rejects",
    },
}


def pick_pipeline(config_path: str) -> dict:
    name = config_path.lower()
    if "wildfire" in name:
        return PIPELINES["wildfire"]
    if "tornado" in name:
        return PIPELINES["tornado"]
    raise ValueError(f"Unknown config type: {config_path}")

__all__ = ["pick_pipeline"]