from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Accessed to index."

@app.route("/", methods=["POST"])
def write_data():
    data = json.loads(request.data)

    data["text"]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False, port=8547)