from influx_helper import influxHelper
import default_settings


def main():
    influx = influxHelper(
        host=default_settings.INFLUXDB_HOST,
        bucket=default_settings.INFLUXDB_BUCKET,
        token=default_settings.INFLUXDB_TOKEN
    )

    influx.load_csv(default_settings.CSV_PATH)
    print("CSV data successfully uploaded to InfluxDB 3")


if __name__ == "__main__":
    main()
