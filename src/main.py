from data_fetcher.openf1_client import fetch_laps_data, fetch_car_data
from data_fetcher.utils import save_data, verify_data

DRIVER_NUMBER = 4  # Lando Norris
SESSION_KEY = 9955  # Carrera en Spielberg


def main():
    print("Downloading lap telemetry data for Lando Norris...")
    laps_df = fetch_laps_data(DRIVER_NUMBER, SESSION_KEY)
    car_df = fetch_car_data(DRIVER_NUMBER, SESSION_KEY)

    save_data(laps_df, DRIVER_NUMBER, SESSION_KEY, "laps")
    save_data(car_df, DRIVER_NUMBER, SESSION_KEY, "car_data")

if __name__ == "__main__":
    main()
