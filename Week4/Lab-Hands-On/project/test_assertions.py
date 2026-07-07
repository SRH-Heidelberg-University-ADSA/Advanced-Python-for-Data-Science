from unittest.mock import Mock
import pytest
from my_assertions import fetch_user

def test_fetch_user_return_value():
    """
    Test that fetch_user returns the expected mocked value.
    """
    mock_api = Mock()
    mock_api.get_user.return_value = {"name": "Alice"}

    result = fetch_user(mock_api)

    # check the returned value
    assert result["name"] == "Alice"

    # verify that get_user() was called exactly once
    mock_api.get_user.assert_called_once()

    # verify that get_user() was called with no arguments
    mock_api.get_user.assert_called_with()

def test_fetch_user_side_effect():
    """
    Test fetch_user with multiple return values using side_effect.
    """
    mock_api = Mock()
    # side_effect returns different results on each call
    mock_api.get_user.side_effect = [{"name": "Alice"}, {"name": "Bob"}]

    # first call returns Alice
    result1 = fetch_user(mock_api)
    assert result1["name"] == "Alice"

    # second call returns Bob
    result2 = fetch_user(mock_api)
    assert result2["name"] == "Bob"

    # verify get_user was called exactly twice
    assert mock_api.get_user.call_count == 2