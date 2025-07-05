import os
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

def save_data(df: pd.DataFrame, driver_number: int, session_key: int, data_type: str) -> None:
    """
    Saves the DataFrame to CSV and Excel files with filenames
    based on driver, session, and data type.
    """
    if verify_data(df):
        base_dir = "telemetry_data"
        driver_folder = os.path.join(base_dir, str(driver_number))
        os.makedirs(driver_folder, exist_ok=True)

        base_filename = f"{driver_number}_telemetry_{data_type}_{session_key}"
        csv_path = os.path.join(driver_folder, f"{base_filename}.csv")
        excel_path = os.path.join(driver_folder, f"{base_filename}.xlsx")

        df.to_csv(csv_path, index=False)
        df.to_excel(excel_path, index=False)
        print(f"Data saved to '{csv_path}' and '{excel_path}'")
    else:
        print(f"No {data_type} data to save.")      

def set_full_display() -> None:
    """Configures pandas to display all rows and columns without truncation."""
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 0)
    pd.set_option('display.max_colwidth', None)