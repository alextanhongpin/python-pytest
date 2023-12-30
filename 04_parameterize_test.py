import pytest


@pytest.mark.parametrize("a, b, c", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test_sum(a, b, c):
    assert a + b == c


@pytest.mark.parametrize("mul", [(1, 2, 2), (2, 3, 6), (3, 4, 12)])
def test_mul(mul):
    a, b, c = mul
    assert a * b == c
