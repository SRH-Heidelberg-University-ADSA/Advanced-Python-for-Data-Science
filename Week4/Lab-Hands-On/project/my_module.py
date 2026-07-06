""""This is a function that depends on an external object (API client), suitable for mocking"""

def fetch_user(api_client):
    """
    Fetch a user from the given API client.
    """
    return api_client.get_user()