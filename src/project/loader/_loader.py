import logging
from sqlalchemy import text
from project.core._db import dbengine

log = logging.getLogger(__name__)


def load_dataframe(df, table_name: str, columns: list[str]) -> None:
    # skip if there's nothing to insert
    if df is None or df.empty:
        log.info("No rows to load -> %s", table_name)
        return

    # make sure required columns exist
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns for {table_name}: {missing}")

    # build parameterized insert statement
    cols = ", ".join(columns)
    values = ", ".join(f":{c}" for c in columns)
    sql = text(f"INSERT INTO {table_name} ({cols}) VALUES ({values})")

    # convert dataframe rows to dictionaries for executemany
    records = df[columns].to_dict(orient="records")

    log.info("Loading %d rows -> %s", len(records), table_name)

    # execute insert inside a transaction
    try:
        with dbengine.begin() as conn:
            conn.execute(sql, records)
        log.info("Loaded %d rows -> %s", len(records), table_name)
    except Exception:
        log.exception("Load failed -> %s", table_name)
        raise


__all__ = ["load_dataframe"]