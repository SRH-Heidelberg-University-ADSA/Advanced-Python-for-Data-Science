"""from square import square

def test_square():
    # verify that the square of 4 is equal to 16
    # if the condition is False, an AssertionError will be raised
    assert square(4) == 16
"""
import pytest
from square import square

@pytest.mark.parametrize(
    "input_value, expected",
    [
        (2, 4),
        (3, 9),
        (0, 0),
        (-4, 16),
        (1.5, 2.25)
    ]
)
def test_square(input_value, expected):
    assert square(input_value) == expected