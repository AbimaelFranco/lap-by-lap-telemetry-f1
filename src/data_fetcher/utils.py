import os
import pandas as pd
from typing import Optional

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

def save_data(df: pd.DataFrame, session_key: int, data_type: str, driver_number: Optional[int] = None) -> None:
    """
    Saves the DataFrame to CSV and Excel files with filenames
    based on driver, session, and data type.
    """
    if verify_data(df):

        split_datetime_column(df)

        base_dir = "telemetry_data"
        driver_folder = os.path.join(base_dir, str(driver_number))
        os.makedirs(driver_folder, exist_ok=True)

        if driver_number is not None:
            base_filename = f"{driver_number}_telemetry_{data_type}_{session_key}"
        else:
            base_filename = f"telemetry_{data_type}_{session_key}"

        csv_path = os.path.join(driver_folder, f"{base_filename}.csv")
        excel_path = os.path.join(driver_folder, f"{base_filename}.xlsx")

        df.to_csv(csv_path, index=False)
        df.to_excel(excel_path, index=False)
        print(f"Data saved to '{csv_path}' and '{excel_path}' \n")
    else:
        print(f"No {data_type} data to save.")      

def set_full_display() -> None:
    """Configures pandas to display all rows and columns without truncation."""
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 0)
    pd.set_option('display.max_colwidth', None)

def split_datetime_column(df: pd.DataFrame) -> pd.DataFrame:
    """Detects the first datetime-like column and splits it into 'date_only' and 'time_only' columns."""
    datetime_col = None

    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            datetime_col = col
            break
        try:
            # Try parsing to datetime without modifying original
            pd.to_datetime(df[col], errors="raise")
            datetime_col = col
            break
        except Exception:
            continue

    if datetime_col is None:
        raise ValueError("No datetime-like column found in the DataFrame.")

    # Convert and strip timezone
    df[datetime_col] = pd.to_datetime(df[datetime_col], errors="coerce", utc=True).dt.tz_convert(None)

    if df[datetime_col].isnull().all():
        raise ValueError(f"Column '{datetime_col}' could not be parsed to datetime.")

    df["date_only"] = df[datetime_col].dt.date
    df["time_only"] = df[datetime_col].dt.time

    return df