import pytest
from math_operations import sum_all

# Basic test functions
def test_sum_all_positive_numbers():
    assert sum_all(1, 2, 3, 4) == 10

def test_sum_all_negative_numbers():
    assert sum_all(-1, -5, -3) == -9

def test_sum_all_no_arguments():
    assert sum_all() == 0

# Parameterized testing for cleaner code
@pytest.mark.parametrize("inputs, expected", [
    ((10, -5, 2), 7),           # Mixed positive and negative
    ((1.5, 2.5, 3.0), 7.0),     # Floats
    ((1.1, -1.1), 0.0),         # Float cancellation
    ((0, 0, 0, 0), 0),          # All zeros
    ((100,), 100),              # Single argument
])
def test_sum_all_variations(inputs, expected):
    assert sum_all(*inputs) == expected

# Testing for expected exceptions
def test_sum_all_type_error():
    with pytest.raises(TypeError, match="All arguments must be integers or floats"):
        sum_all(1, 2, "three")