import pytest
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@pytest.mark.great
def test_greater():
    num = 100
    logger.info(f"{num} is greater than provided number")
    # logger.log()
    assert num > 99.9999999999999


@pytest.mark.great
def test_greater_equal():
    num = 100
    logger.info(f"{num} is equal to provided number")
    assert num >= 100
