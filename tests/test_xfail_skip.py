# Pytest - Xfail/Skip Tests:
import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num < 99.9999999999999

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
    num = 10
    assert num < -10.000000000000011111

@pytest.mark.skip
@pytest.mark.others
def test_less_equal():
    num = 10
    assert num <= 10
