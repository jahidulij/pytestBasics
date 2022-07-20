# Pytest - conftest.py:
import pytest


def test_conf_divisible_by_13(input_value):
    assert input_value % 13 == 0
