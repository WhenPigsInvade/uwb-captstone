import os
import dash
from dash import dcc, html
import plotly.express as px
from influxdb_client_3 import InfluxDBClient3

# ------------------------
# InfluxDB 3 connection
# ------------------------
client = InfluxDBClient3(
    host="http://localhost:8181",
    database="plantbuddy",
    token=os.environ.get("INFLUXDB3_AUTH_TOKEN")
)

# ------------------------
# Query sensor data
# ------------------------
query = """
SELECT *
FROM sensor_data
ORDER BY time
"""

# Convert Arrow → Pandas
df = client.query(query).to_pandas()

# ------------------------
# Dash app
# ------------------------
app = dash.Dash(__name__)

graphs = []

exclude_cols = {"time", "device_id"}

for column in df.columns:
    if column in exclude_cols:
        continue

    sensor_df = df[df[column].notna()]
    if sensor_df.empty:
        continue

    fig = px.line(
        sensor_df,
        x="time",
        y=column,
        title=column.replace("_", " ").title()
    )

    graphs.append(dcc.Graph(figure=fig))

app.layout = html.Div(
    children=[
        html.H1("PlantBuddy Sensor Data"),
        *graphs
    ],
    style={"width": "90%", "margin": "auto"}
)

if __name__ == "__main__":
    app.run(debug=True)
