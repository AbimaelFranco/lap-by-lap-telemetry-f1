from data_fetcher.openf1_client import fetch_laps_data
import pandas as pd
from data_fetcher.utils import verify_data, save_data

DRIVER_NUMBER = 81  # Lando Norris
SESSION_KEY = 9955  # Carrera en Spielberg


def main():
    print("Descargando telemetría de vueltas para Lando Norris...")
    df = fetch_laps_data(DRIVER_NUMBER, SESSION_KEY)

    save_data(df, DRIVER_NUMBER, SESSION_KEY)

if __name__ == "__main__":
    main()
