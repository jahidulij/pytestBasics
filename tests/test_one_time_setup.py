import pytest


@pytest.mark.trylast
def test_methodA(oneTimeSetUp, setUp):
    print("Running test method A")

@pytest.mark.tryfirst
def test_methodB(oneTimeSetUp, setUp):
    print("Running test method B")


def test_methodC(oneTimeSetUp, setUp):
    print("Running test method C")


def test_methodD(oneTimeSetUp, setUp):
    print("Running test method D")


def test_methodE(oneTimeSetUp, setUp):
    print("Running test method E")


def test_methodF(oneTimeSetUp, setUp):
    print("Running test method F")
