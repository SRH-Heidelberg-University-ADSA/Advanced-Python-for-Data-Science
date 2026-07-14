import pickle

from flask import Flask, jsonify, request

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def index():
    return jsonify(
        {
            "api": "predict stock values",
            "endpoints": "POST /model to predict, GET to /model to get params",
        }
    )


@app.route("/model", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "x" not in data:
        return jsonify({"error": "missing x or incorrect json"})

    input = data["x"]

    prediction = model.predict([[input]])[0]

    return jsonify({"prediction": round(prediction, 3)})


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
