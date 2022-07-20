# Pytest - conftest.py:
import pytest
# Log:
import logging

logging.basicConfig(filename="C:/Users/JahidulIslam/PycharmProjects/pytestTutorialPoints/logs/test.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.DEBUG
                    )
@pytest.fixture
def input_value():
    input = 72
    return input

