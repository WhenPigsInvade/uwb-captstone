import os

INFLUXDB_HOST = "http://localhost:8181"
INFLUXDB_BUCKET = "plantbuddy"

INFLUXDB_TOKEN = os.getenv("INFLUXDB3_AUTH_TOKEN")

CSV_PATH = "./data/one_hour.csv"
