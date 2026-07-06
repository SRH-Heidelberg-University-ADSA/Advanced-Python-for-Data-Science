from unittest.mock import mock_open, patch
from my_patch import read_file

def test_read_file():
    # Sample content we want the file to "contain"
    mock_content = "Hello, world!"
    
    # patch 'builtins.open' with a mock that simulates file reading
    with patch("builtins.open", mock_open(read_data=mock_content)) as mocked_file:
        result = read_file("file.txt")  # path is irrelevant; the file is mocked
        # assert that the function returns the mocked content
        assert result == mock_content

        # optional: check that open was called with the correct path and mode
        mocked_file.assert_called_once_with("file.txt", "r")