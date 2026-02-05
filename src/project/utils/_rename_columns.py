def rename_columns(df, source):
    df = df[list(source.columns.keys())].rename(columns=source.columns)
    insert_cols = list(source.columns.values())
    return df, insert_cols

__all__ = ["rename_columns"]