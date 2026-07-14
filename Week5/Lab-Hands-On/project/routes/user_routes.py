# Blueprint: a Flask feature for organizing routes into modular, reusable components.
# Instead of registering routes directly on the app, they are grouped on a Blueprint
# and later registered on the app via app.register_blueprint().
from flask import Blueprint, request, jsonify

# Create a Blueprint instance named 'user_bp'.
# Argument 1 - 'user_bp': the internal name Flask uses to identify this blueprint
#   (used in url_for() calls, e.g. url_for('user_bp.get_users'))
# Argument 2 - __name__: tells Flask where this blueprint's resources are located,
#   same role as in Flask(__name__)
user_bp = Blueprint('user_bp', __name__)

# In-memory user store scoped to this blueprint module.
# Since this lives at the module level, it is shared across all requests
# handled by this blueprint for the lifetime of the server process.
users = []

# Route: GET /
# The path "/" here is relative — its full URL depends on the prefix assigned
# when this blueprint is registered. For example, if registered with
# url_prefix="/users", this route becomes GET /users/
@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(users)  # Return the full users list as a JSON array

# Route: POST /
# Accepts a JSON body and appends the parsed data to the users list.
# Again, the full URL is determined at registration time via url_prefix.
@user_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()  # Deserialize the incoming JSON request body
    users.append(data)         # Add the new user dict to the in-memory list
    return jsonify({"message": "User added"}), 201  # 201 = resource created successfully