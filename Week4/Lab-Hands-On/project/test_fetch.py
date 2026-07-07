from unittest.mock import Mock
from my_module import fetch_user

def test_fetch_user():
    # create a mock API client
    mock_api = Mock()
    
    # define what get_user() should return
    mock_api.get_user.return_value = {"name": "Alice"}
    
    # call the function with the mock
    result = fetch_user(mock_api)
    
    # assert that the function returns the mocked value
    assert result["name"] == "Alice"