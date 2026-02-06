from flask import Flask, jsonify
from influxdb import InfluxDBClient
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
import datetime


# @TODO Move to own config file
# ----------------------------
# Configuration
# ----------------------------
INFLUX_URL = "http://localhost:69"
INFLUX_ORG = "exawater"
INFLUX_BUCKET = "sensor-data"

SERVICE_PORT = 420

CSV_FILE = "data/data.csv"
MEASUREMENT = "environment"

app = Flask(__name__)
client = InfluxDBClient(
    url=INFLUX_URL,
    org=INFLUX_ORG
)

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

@app.route("/data", methods=['GET'])
def get_data():
    message = {"time": datetime.datetime.now(),
               "temperature": "TODO",
               "humidity": "TODO"
               }
    return jsonify(message)

@app.route("/prediction", methods=['GET'])
def get_prediction():
    message = {"prediction": "TODO"}
    return jsonify(message)

# @TODO
def read_sensors():
    return

# @TODO
def read_database():
    return


# ----------------------------
# Load CSV
# ----------------------------
def load_csv_to_influx():
    print("Loading CSV data into InfluxDB...")

    df = pd.read_csv(CSV_FILE)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    points = []

    for _, row in df.iterrows():
        point = (
            Point(MEASUREMENT)
            .field("temperature", float(row["temperature"]))
            .field("humidity", float(row["humidity"]))
            .time(row["timestamp"], WritePrecision.NS)
        )
        points.append(point)

    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=points)

    print("CSV successfully loaded.")

# ----------------------------
# Startup
# ----------------------------
with app.app_context():
    load_csv_to_influx()


if __name__ == "__main__":
    app.run(port=SERVICE_PORT)