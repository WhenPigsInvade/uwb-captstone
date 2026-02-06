import pandas as pd
from influxdb_client_3 import InfluxDBClient3


class influxHelper:
    def __init__(self, host: str, bucket: str, token: str):
        self.client = InfluxDBClient3(
            host=host,
            database=bucket,
            token=token
        )

    def load_csv(self, csv_path: str):
        df = pd.read_csv(csv_path)
        df["time"] = pd.to_datetime(df["time"])

        points = []
        

        for _, row in df.iterrows():
            point = {
                "measurement": "sensor_data",
                "tags": {
                    "device_id": row["device_id"]
                },
                "fields": {
                    row["sensor_type"]: float(row["value"])
                },
                "time": row["time"]
            }
            points.append(point)

        self.client.write(points)

    def querydata(self, sensor_name: str, device_id: str):
        sql = f"""
        SELECT time, {sensor_name}
        FROM sensor_data
        WHERE device_id = '{device_id}'
        ORDER BY time
        """
        return self.client.query(query=sql, language="sql").to_pandas()
