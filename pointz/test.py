import pytest


def test_basic():
    assert 1 == 1


def soma(x, y):
    return 3


@pytest.mark.parametrize(
    'resultado,x,y',
    [
        [3, 1, 2],
        [4, 1, 3],
    ]
)
def test_soma(resultado, x, y):
    assert resultado == soma(x, y)
