import requests
import pandas as pd
from typing import Optional

API_BASE = "https://api.openf1.org/v1"
HEADERS = {}

def fetch_laps_data(session_key: int, driver_number: int) -> pd.DataFrame:
    """Downloads the telemetry data for each lap of a driver in a given session."""
    url = f"{API_BASE}/laps"
    params = {"driver_number": driver_number, "session_key": session_key}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df

def fetch_car_data(session_key: int, driver_number: int) -> pd.DataFrame:
    """Downloads the car data for a driver in a given session."""
    url = f"{API_BASE}/car_data"
    params = {"driver_number": driver_number, "session_key": session_key}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df

def fetch_drivers_data(session_key: int, driver_number: Optional[int] = None) -> pd.DataFrame:
    """Downloads the drivers data in a given session."""
    url = f"{API_BASE}/drivers"

    if driver_number is not None:
        params = {"session_key": session_key, "driver_number": driver_number}
    else:
        params = {"session_key": session_key}

    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df

def fetch_intervals_data(session_key: int, driver_number: int) -> pd.DataFrame:
    """Downloads the intervals data in a given session."""
    url = f"{API_BASE}/intervals"
    params = {"driver_number": driver_number, "session_key": session_key}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df