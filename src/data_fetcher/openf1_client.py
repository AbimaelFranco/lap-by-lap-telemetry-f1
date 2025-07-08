import requests
import pandas as pd

API_BASE = "https://api.openf1.org/v1"
HEADERS = {}

def fetch_laps_data(driver_number: int, session_key: int) -> pd.DataFrame:
    """Downloads the telemetry data for each lap of a driver in a given session."""
    url = f"{API_BASE}/laps"
    params = {"driver_number": driver_number, "session_key": session_key}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df

def fetch_car_data(driver_number: int, session_key: int) -> pd.DataFrame:
    """Downloads the car data for a driver in a given session."""
    url = f"{API_BASE}/car_data"
    params = {"driver_number": driver_number, "session_key": session_key}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df

def fetch_drivers_data(session_key: int) -> pd.DataFrame:
    """Downloads the drivers data in a given session."""
    url = f"{API_BASE}/drivers"
    params = {"session_key": session_key}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df

def fetch_intervals_data(driver_number: int, session_key: int) -> pd.DataFrame:
    """Downloads the intervals data in a given session."""
    url = f"{API_BASE}/intervals"
    params = {"driver_number": driver_number, "session_key": session_key}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df