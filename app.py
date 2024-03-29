from flask import Flask, request, jsonify
import json, cv2

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Accessed to index."

# LETTER
@app.route("/letter", methods=["GET"])
def letter():
    return "Accessed to letter audio recognizer."

@app.route("/letter", methods=["POST"])
def recognize_letters_by_audio():
    # data = json.loads(request.data)

    return jsonify(rd.choice([True, False]))

if __name__ == "__main__":
    app.run_server(debug=False, port=8547)
