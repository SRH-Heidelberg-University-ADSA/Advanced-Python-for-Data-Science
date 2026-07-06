from unittest.mock import Mock
from my_side_effects import fetch_user

def test_fetch_user_side_effect():
    # create a mock API client
    mock_api = Mock()
    
    # side_effect returns a sequence of values each time get_user() is called
    mock_api.get_user.side_effect = [
        {"name": "Alice"}, 
        {"name": "Bobb"}
    ]
    
    # first call returns Alice
    result1 = fetch_user(mock_api)
    assert result1["name"] == "Alice"
    
    # second call returns Bob
    result2 = fetch_user(mock_api)
    assert result2["name"] == "Bob"