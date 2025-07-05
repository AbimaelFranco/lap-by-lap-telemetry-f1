import pandas as pd

def verify_data(df: pd.DataFrame):
    """Verifies if the DataFrame is empty and shows useful info."""
    if df.empty:
        print("No telemetry data found.")
    else:
        set_full_display()
        num_rows = len(df)
        num_cols = len(df.columns)
        column_list = ', '.join(df.columns)

        print(f"DataFrame contains {num_rows} rows and {num_cols} columns.")
        print(f"Got the columns: {column_list}")

def set_full_display():
    """Configures pandas to display all rows and columns without truncation."""
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 0)
    pd.set_option('display.max_colwidth', None)