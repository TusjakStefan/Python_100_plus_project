import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# from src.calculator import addition
from calculator import addition
import pytest

@pytest.mark.parametrize("number1, number2, expected", [
    (2, 3, 5),
    (2, -5, -3),
    (-2, 5, 3),
    (-2, -5, -7),
    (2.3, 5.2, 7.5),
    (2.3, -5.2, -2.9)
])
def test_addition(number1, number2, expected):
    assert addition(number1, number2) == expected