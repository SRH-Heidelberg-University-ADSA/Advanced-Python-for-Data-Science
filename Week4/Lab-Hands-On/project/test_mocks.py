from unittest.mock import patch
from my_mocks import store_data

def test_store_data_mocked_class():
    """
    Test store_data by mocking the Database class entirely.
    """
    # Patch 'Database' in the 'my_mocks' module
    with patch("my_mocks.Database") as MockDatabase:
        # Create a mock instance (this replaces the real Database instance)
        db_instance = MockDatabase()

        # Define the return value of the save() method
        db_instance.save.return_value = True

        # Call the function with the mock instance
        result = store_data(db_instance, {"id": 1, "name": "Alice"})

        # Assert that the function returns True
        assert result is True

        # Verify that save() was called exactly once with the correct argument
        db_instance.save.assert_called_once_with({"id": 1, "name": "Alice"})