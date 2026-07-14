# Import the Flask class, request object, and jsonify utility from the flask library.
# - Flask: creates the web application instance
# - request: provides access to incoming HTTP request data (headers, body, etc.)
# - jsonify: converts Python dicts/lists into JSON HTTP responses
from flask import Flask, request, jsonify

# Create a Flask application instance.
# __name__ tells Flask where to look for resources (templates, static files, etc.)
app = Flask(__name__)

# In-memory "database" to store user records.
# Note: This list resets every time the server restarts. Thus, **not suitable** for production.
users = []

# Route: GET /users
# Returns the full list of users as a JSON array.
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Route: POST /users
# Expects a JSON body (e.g. {"name": "Alice", "email": "alice@example.com"}).
# Appends the parsed data to the users list and responds with a 201 Created status.
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()  # Parse the incoming JSON request body into a Python dict
    users.append(data)         # Add the new user dict to the in-memory list
    return jsonify({"message": "User added"}), 201  # 201 = resource successfully created

# Entry point: only runs when this script is executed directly (not imported as a module).
# - debug=True: enables auto-reloading and detailed error pages during development
# - use_reloader=False: disables the Werkzeug reloader (useful in some IDE/notebook environments
#   to prevent the app from spawning a duplicate process)
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)