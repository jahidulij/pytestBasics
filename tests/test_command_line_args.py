import pytest


@pytest.mark.trylast
def test_methodA(oneTimeSetUp, setUp):
    print("Running test method A")

@pytest.mark.tryfirst
def test_methodB(oneTimeSetUp, setUp):
    print("Running test method B")



