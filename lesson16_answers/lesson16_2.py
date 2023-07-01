def add_numbers(num1, num2):
    return num1 + num2

import pytest
from your_module import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5  # Test with positive numbers
    assert add_numbers(-5, 10) == 5  # Test with positive and negative numbers
    assert add_numbers(0, 0) == 0  # Test with zeros
    assert add_numbers(2.5, 1.5) == 4.0  # Test with floating-point numbers
    assert add_numbers(9999999999999999999, 1) == 10000000000000000000  # Test with large numbers

if __name__ == '__main__':
    pytest.main()
