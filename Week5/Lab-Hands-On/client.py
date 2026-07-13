import requests

# Base URL of the running Flask server.
# Ensure server.py is running before executing this script.
BASE_URL = "http://127.0.0.1:5000"

# --- Step 1: Login and retrieve JWT ---

# Credentials sent to the /login endpoint.
# In production these would come from user input or environment variables.
login_payload = {"username": "student", "password": "pass123"}

# POST credentials to /login & server validates and returns a signed JWT.
login_response = requests.post(f"{BASE_URL}/login", json=login_payload)

if login_response.status_code == 200:
    # Extract the JWT string from the response body.
    token = login_response.json()["access_token"]
    print("Login successful! Token:", token)
else:
    # No token means no access & exit rather than sending invalid requests.
    print("Login failed:", login_response.json())
    exit()

# --- Step 2: Access protected route with JWT ---

# Attach the JWT to the Authorization header using the Bearer scheme.
# Format: Authorization: Bearer <token>
headers = {"Authorization": f"Bearer {token}"}

# GET /protected : server validates the token before granting access.
protected_response = requests.get(f"{BASE_URL}/protected", headers=headers)

if protected_response.status_code == 200:
    print("Protected route response:", protected_response.json())
else:
    print("Failed to access protected route:", protected_response.json())
