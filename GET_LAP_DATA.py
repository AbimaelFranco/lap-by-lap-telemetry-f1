import requests
import pandas as pd

API_BASE = "https://api.openf1.org/v1"
DRIVER_NUMBER = 4  # Lando Norris
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

def main():
    print("Descargando telemetría de vueltas para Lando Norris...")
    df = fetch_laps_data(DRIVER_NUMBER, SESSION_KEY)

    if df.empty:
        print("No se encontraron datos de telemetría.")
    else:
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 0)
        pd.set_option('display.max_colwidth', None)

        print(df.head())  # Muestra filas específicas para evitar saturación
        df.to_csv("norris_telemetria_laps_9955.csv", index=False)
        df.to_excel("norris_telemetria_laps_9955.xlsx", index=False)
        print(f"Datos guardados en '{DRIVER_NUMBER}_telemetria_{SESSION_KEY}.csv' y en '{DRIVER_NUMBER}_telemetria_{SESSION_KEY}.xlsx'  ({len(df)} filas)")


if __name__ == "__main__":
    main()
