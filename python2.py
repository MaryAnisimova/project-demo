from flask import Flask, jsonify
import time
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    timestamp = int(time.time())
    message = "Automate all the things!"
    dt_object = datetime.fromtimestamp(timestamp)
    return jsonify({"message": message, "timestamp": timestamp, "human_readable_timestamp": dt_object})


if __name__ == '__main__':
    app.run()


