from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

# --- App Setup ---
app = Flask(__name__)

# Secret key used to sign and verify JWT tokens.
# In production, store this in an environment variable & NEVER hardcode it.
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Bind JWTManager to the app: handles JWT configuration
# and automatic error responses for invalid or missing tokens.
jwt = JWTManager(app)

# Single hardcoded user for demonstration ONLY.
# In production, users are stored in a database with hashed passwords.
USER = {"username": "student", "password": "pass123"}

# Route: GET /
# Health check endpoint to confirm the server is running.
@app.route("/", methods=["GET"])
def index():
    return "Flask JWT server is running!"

# Route: POST /login
# Public endpoint: validates credentials and returns a signed JWT on success.
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    # Reject requests with missing fields before any credential checking.
    if not data or "username" not in data or "password" not in data:
        return jsonify({"msg": "Missing username or password"}), 400

    # Validate credentials against the known user.
    if data["username"] == USER["username"] and data["password"] == USER["password"]:
        # Generate a signed JWT embedding the username as the token's identity.
        access_token = create_access_token(identity=data["username"])
        return jsonify(access_token=access_token)

    # Vague error message intentional to avoid revealing which field was wrong.
    return jsonify({"msg": "Bad credentials"}), 401

# Route: GET /protected
# @jwt_required() validates the JWT from the Authorization header
# before the function body executes & returns 401 if invalid or missing.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"message": "Access granted"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)