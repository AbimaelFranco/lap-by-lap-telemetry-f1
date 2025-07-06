from data_fetcher.openf1_client import fetch_laps_data, fetch_car_data, fetch_drivers_data
from data_fetcher.utils import save_data, verify_data, split_datetime_column

DRIVER_NUMBER = 4  # Lando Norris
SESSION_KEY = 9955  # Carrera en Spielberg


def main():
    print("Downloading lap telemetry data for Lando Norris...")
    laps_df = fetch_laps_data(DRIVER_NUMBER, SESSION_KEY)
    car_df = fetch_car_data(DRIVER_NUMBER, SESSION_KEY)
    drivers_df = fetch_drivers_data(SESSION_KEY)

    save_data(laps_df, SESSION_KEY, "laps", DRIVER_NUMBER)
    save_data(car_df, SESSION_KEY, "car_data", DRIVER_NUMBER)
    save_data(drivers_df, SESSION_KEY, "drivers")

if __name__ == "__main__":
    main()
