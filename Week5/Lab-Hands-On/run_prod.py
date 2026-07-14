from flask import Flask, jsonify
from waitress import serve

# Create Flask app
app = Flask(__name__)

# Routes
@app.route("/")
def home():
    return jsonify({"message": "Dockerised production server running"})

@app.route("/users")
def users():
    return jsonify([
    {"id": 1, "name": "Harry"},
    {"id": 2, "name": "Styles"},
    {"id": 3, "name": "Tom"},
    {"id": 4, "name": "Cruise"}
    ])

# Entry point for Waitress
if __name__ == "__main__":
    print("========================================")
    print("Starting self-contained Dockerised Flask production server")
    print("Serving on http://0.0.0.0:5000")
    print("========================================")
    serve(app, host="0.0.0.0", port=5000)