# Import Flask for creating the web application
# and jsonify for returning JSON responses.
from flask import Flask, jsonify

# Import os to access environment variables.
import os

# Create the Flask application.
app = Flask("Week6 Cloud App")


# Read the application version from an environment variable.
# Used later to verify Kubernetes configuration updates.
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")


# Define the main API endpoint.
@app.route("/", methods=["GET"])
def home():
    # Return application information as JSON.
    return jsonify({
        "message": "Week 6 - Cloud Deployment & DevOps",
        "version": APP_VERSION
    })


# Health-check endpoint used by Kubernetes probes.
@app.route("/health", methods=["GET"])
def health():
    # Return HTTP 200 to indicate the service is healthy.
    return jsonify({"status": "ok"}), 200


# Start the Flask server when the file is executed directly.
if __name__ == "__main__":

    # 0.0.0.0 allows access from Docker/Kubernetes containers.
    app.run(host="0.0.0.0", port=5000)