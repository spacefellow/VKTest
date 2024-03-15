import pytest


testdata = [
    ([1, 2, 3], 3),
    ([], 0)
]

@pytest.mark.parametrize("test_list, length", testdata)
def test_list_length(test_list, length):
    assert len(test_list) == length



testdata = [1, [1], {1:1}, (1), None, True, 1.0]

@pytest.mark.parametrize("data", testdata)
def test_float_summ(data):
    try:
        assert [1] + data
    except TypeError:
        pass