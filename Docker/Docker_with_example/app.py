from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

# Load environment variables from .env (optional)
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    # Read an environment variable
    app_name = os.getenv("APP_NAME", "Basic Docker Python App")

    # Get current UTC time
    utc_time = datetime.now(pytz.UTC).strftime("%Y-%m-%d %H:%M:%S")

    # Make a very simple HTTP request
    response = requests.get("https://httpbin.org/get")

    return jsonify({
        "app": app_name,
        "time_utc": utc_time,
        "http_status_from_httpbin": response.status_code
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
