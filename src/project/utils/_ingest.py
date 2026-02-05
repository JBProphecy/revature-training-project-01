import logging
import pandas as pd

from project.utils import load_config_from_yaml, load_external_data
from project.loader._loader import load_dataframe

from project.utils._pick_pipeline import pick_pipeline
from project.utils._rename_columns import rename_columns


log = logging.getLogger(__name__)


def ingest(config_path: str) -> None:
    pipeline = pick_pipeline(config_path)

    config = load_config_from_yaml(config_path)
    source = config.sources[0]

    log.info("\nIngesting %s", config_path)
    log.info("Source file: %s", source.path)

    # read
    df = load_external_data(config, 0)
    log.info("Read %d rows", len(df))

    # rename
    df, insert_cols = rename_columns(df, source)
    log.info("Columns renamed")

    # clean
    df = pipeline["clean"](df)
    log.info("Data cleaned")

    # limit dataset size for tornado
    if "tornado" in config_path.lower():
        df = df[df["year"].between(2010, 2015)]
        log.info("Filtered tornado to years 2010–2015: %d rows", len(df))

    # dedupe
    accepted_after_dedupe, dup_rejects = pipeline["dedupe"](df)
    log.info("Deduped: %d rows remain", len(accepted_after_dedupe))

    # validate
    accepted, rejected = pipeline["validate"](accepted_after_dedupe)
    log.info("Validated: %d accepted, %d rejected", len(accepted), len(rejected))

    # merge duplicate rejects
    if dup_rejects is not None and not dup_rejects.empty:
        rejected = pd.concat([rejected, dup_rejects], ignore_index=True)

    # load accepted
    load_dataframe(accepted, pipeline["accepted_table"], insert_cols)
    log.info("Loaded accepted -> %s", pipeline["accepted_table"])

    # load rejected
    if rejected is not None and not rejected.empty:
        load_dataframe(rejected, pipeline["rejects_table"], insert_cols + ["reason"])
        log.info("Loaded rejected -> %s", pipeline["rejects_table"])
    else:
        log.info("No rejected rows to load")

    log.info("Finished %s\n", pipeline["accepted_table"])

__all__ = ["ingest"]