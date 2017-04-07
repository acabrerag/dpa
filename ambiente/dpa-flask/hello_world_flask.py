import os
import json

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({ "mensaje": "Hola desde Flask (dentro de docker)" })

if __name__ == "__main__":
    port = int(os.environ.get("API_PORT", 5000))
    app.run(host="0.0.0.0", port = port)
