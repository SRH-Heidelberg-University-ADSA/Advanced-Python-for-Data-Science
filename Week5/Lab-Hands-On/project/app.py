from flask import Flask

# Import the user Blueprint defined in routes/user_routes.py.
# This assumes the following project structure:
#   project/
#   ├── app.py              ← this file
#   └── routes/
#       ├── __init__.py     ← makes 'routes' a Python package (can be empty)
#       └── user_routes.py  ← defines user_bp
from routes.user_routes import user_bp

# Create the central Flask application instance.
# __name__ helps Flask locate resources relative to this file's directory.
app = Flask(__name__)

# Register the user Blueprint onto the main app.
# - user_bp: the Blueprint object imported above
# - url_prefix="/users": prepends "/users" to all routes defined in the blueprint,
#   so user_bp's "/" becomes "/users/",
#   and any future route like "/profile" would become "/users/profile"
app.register_blueprint(user_bp, url_prefix="/users")

# Entry point: only executes when this file is run directly (e.g. python app.py).
# Importing this file as a module (e.g. in tests) will NOT trigger app.run().
# - debug=True: enables hot-reloading on file changes and detailed error pages.
#   Never use debug=True in production — it exposes an interactive debugger.
if __name__ == "__main__":
    app.run(debug=True)
