import pytest


testdata = [
    (0, 1), 
    (2, 3), 
    (-1, 5)
]

@pytest.mark.parametrize("index, expected_value", testdata)
def test_tuple_indexing(index, expected_value):
    my_tuple = (1, 2, 3, 4, 5)
    assert my_tuple[index] == expected_value



def test_tuple_negative_indexing():
    my_tuple = (1, 2, 3)
    try:
        value = my_tuple[3]
    except IndexError:
        pass