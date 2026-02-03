from flask import Flask, jsonify
import datetime

app = Flask(__name__)

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

# TODO
def read_sensors():
    return

# TODO
def read_database():
    return

if __name__ == "__main__":
    app.run(port=420)