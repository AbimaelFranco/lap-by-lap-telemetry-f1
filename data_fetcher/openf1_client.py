import requests
import pandas as pd

API_BASE = "https://api.openf1.org/v1"
DRIVER_NUMBER = 81  # Lando Norris
SESSION_KEY = 9955  # Carrera en Spielberg
HEADERS = {}

def fetch_laps_data(driver_number: int, session_key: int) -> pd.DataFrame:
    """Descarga la telemetría del piloto para una sesión dada."""
    url = f"{API_BASE}/laps"
    params = {"driver_number": driver_number, "session_key": session_key}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    return df