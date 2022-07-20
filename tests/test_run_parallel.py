# Pytest - Run Tests in Parallel
# Pytest - Parameterizing Tests:
import pytest


@pytest.mark.parametrize("num, output",
                         [
                             (1, 11),
                             (2, 22),
                             (3, 33),
                             (4, 43)
                         ])
def test_multiplication_11(num, output):
    assert 11 * num == output
