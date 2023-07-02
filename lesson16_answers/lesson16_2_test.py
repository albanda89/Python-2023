import pytest
from lesson16_2 import add_numbers

#def add_numbers(num1, num2):
#    return num1 + num2

@pytest.mark.parametrize("num1, num2, expected_sum", [
    (1, 2, 3),
    (-5, 10, 5),
    (0, 0, 0),
    (100, -100, 0),
    (7, 7, 14),
])
def test_add_numbers(num1, num2, expected_sum):
    assert add_numbers(num1, num2) == expected_sum
