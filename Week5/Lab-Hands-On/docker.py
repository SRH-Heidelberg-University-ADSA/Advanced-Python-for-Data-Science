from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Dockerised local server running"})

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Harry"},
        {"id": 2, "name": "Styles"}
    ])

if __name__ == "__main__":
    # Local development only
    print("========================================")
    print("Starting self-contained Dockerised Flask local server")
    print("Serving on http://0.0.0.0:5000")
    print("========================================")
    app.run(debug=True, host="0.0.0.0", port=5000)