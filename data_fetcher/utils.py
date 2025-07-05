import pandas as pd

def verify_data(df: pd.DataFrame) -> bool:
    """Verifies if the DataFrame is empty and shows useful info."""
    if df.empty:
        print("No telemetry data found.")
        return False
    else:
        set_full_display()
        num_rows = len(df)
        num_cols = len(df.columns)
        column_list = ', '.join(df.columns)

        print(f"Telemetry contains {num_rows} rows and {num_cols} columns.")
        print(f"Got the columns: {column_list}")
        return True

def save_data(df: pd.DataFrame, driver_number: int, session_key: int) -> None:
    """Saves the DataFrame to CSV and Excel files."""
    if verify_data(df):
        csv_filename = f"{driver_number}_telemetry_laps_{session_key}.csv"
        excel_filename = f"{driver_number}_telemetry_laps_{session_key}.xlsx"

        df.to_csv(csv_filename, index=False)
        df.to_excel(excel_filename, index=False)
        print(f"Data saved to '{csv_filename}' and '{excel_filename}'")
    else:
        print("No data to save.")
        

def set_full_display() -> None:
    """Configures pandas to display all rows and columns without truncation."""
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 0)
    pd.set_option('display.max_colwidth', None)