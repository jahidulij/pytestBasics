# Run pytest from terminal:
import math


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_square():
    num = 7
    assert num * num == 49


def test_equality():
    assert 11 == 11
