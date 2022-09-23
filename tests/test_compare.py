# Run pytest from terminal:
import pytest


@pytest.mark.great
def test_greater():
    num = 100
    assert num > 99.9999999999999


@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.others
def test_less():
    num = 10
    assert num < 10.000000000000011112


@pytest.mark.others
def test_less_equal():
    num = 10
    assert num <= 10
