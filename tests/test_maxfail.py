# Pytest - Stop Test Suite after N Test Failures
import pytest
import math


def test_sqrt_failure():
    assert math.sqrt(25) == 6


def test_sqare_failure():
    assert 7 * 7 == 77


def test_equality_failure():
    assert 23 == 32
