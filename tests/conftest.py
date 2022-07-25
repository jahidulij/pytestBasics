# Pytest - conftest.py:
import pytest
# Log:
import logging

logging.basicConfig(filename="C:/Users/JahidulIslam/PycharmProjects/pytestBasics/logs/test.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.DEBUG
                    )


@pytest.fixture
def input_value():
    input = 72
    return input


@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level teardown")


@pytest.fixture(scope="module")
def oneTimeSetUp(browser, osType):
    print("Running one time setup")
    if browser.lower() == "chrome":
        print("Running tests on chrome")
    elif browser.lower() == "firefox":
        print("Running tests on firefox")
    else:
        print("Browser not supported")

    if osType.lower() == "windows":
        print("Running tests on windows")
    elif osType.lower() == "mac":
        print("Running tests on mac")
    elif osType.lower() == "linux":
        print("Running tests on linux")
    else:
        print("Operating system not supported")
    yield
    print("Running one time teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--ostype")
