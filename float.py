import pytest


testdata = [
    (-1.0, 0, 0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, 1.0),
    (1.0, 0, 0),
    (-1.0, -1.0, 1.0),
]

@pytest.mark.parametrize("num1, num2, expected", testdata)
def test_float_multiplication(num1, num2, expected):
    result = num1 * num2
    assert result == expected


testdata = [1, [1], {1:1}, (1), None, True, 1.0]

@pytest.mark.parametrize("data", testdata)
def test_float_isinstance(data):
    try:
        assert 1.0 + data
    except TypeError:
        pass
