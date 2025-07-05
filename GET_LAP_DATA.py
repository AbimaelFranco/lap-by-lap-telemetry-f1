from data_fetcher.openf1_client import fetch_laps_data
import pandas as pd

DRIVER_NUMBER = 81  # Lando Norris
SESSION_KEY = 9955  # Carrera en Spielberg


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
        df.to_csv(f"{DRIVER_NUMBER}_telemetria_laps_{SESSION_KEY}.csv", index=False)
        df.to_excel(f"{DRIVER_NUMBER}_telemetria_laps_{SESSION_KEY}.xlsx", index=False)
        print(f"Datos guardados en '{DRIVER_NUMBER}_telemetria_{SESSION_KEY}.csv' y en '{DRIVER_NUMBER}_telemetria_{SESSION_KEY}.xlsx'  ({len(df)} filas)")


if __name__ == "__main__":
    main()
