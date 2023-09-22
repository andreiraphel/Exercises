# Import the factorial function to be tested
import pytest
from factorial import factorial

# Write test cases using pytest
def test_factorial_of_zero():
    assert factorial(0) == 1

def test_factorial_of_one():
    assert factorial(1) == 1

def test_factorial_of_positive_number():
    assert factorial(5) == 120

def test_factorial_of_negative_number():
    # Negative numbers don't have factorials, so we expect an exception.
    with pytest.raises(ValueError):
        factorial(-5)