# Markers:
import math
import pytest


@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.square
def test_square():
    num = 7
    assert num * num == 49


@pytest.mark.others
def test_equality():
    assert 11 == 11
