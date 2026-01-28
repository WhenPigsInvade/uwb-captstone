from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/fetch-data", methods=['GET'])
def fetch_data():
    message = {"message": "TODO"}
    return jsonify(message)

# TODO
def read_sensors():
    return

# TODO
def read_database():
    return

if __name__ == "__main__":
    app.run(port=420)