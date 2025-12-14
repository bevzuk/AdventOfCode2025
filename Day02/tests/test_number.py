import pytest
from src.number import Number

@pytest.mark.parametrize("number,expected_power", [
    (0, 0),
    (1, 1),
    (10, 2),
    (11, 2),
    (20, 2),
    (99, 2),
    (100, 3),
    (999, 3),
    (1000, 4),
    (1000000, 7),
])
def test_power(number, expected_power):
    n = Number(number)
    assert n.power() == expected_power

@pytest.mark.parametrize("number,expected_right", [
    (10, 0),
    (20, 0),
    (1122, 22),
    (123124, 124),
    (5, 5),
    (125, 25),
    (12345, 345),
])
def test_right(number, expected_right):
    n = Number(number)
    assert n.right() == expected_right

@pytest.mark.parametrize("number,expected_left", [
    (10, 1),
    (20, 2),
    (1122, 11),
    (123124, 123),
    (5, 0),
    (12345, 12),
])
def test_left(number, expected_left):
    n = Number(number)
    assert n.left() == expected_left

@pytest.mark.parametrize("number,split_length,expected", [
    (11, 1, ["1", "1"]),
    (12, 1, ["1", "2"]),
    (123, 1, ["1", "2", "3"]),
    (1234, 1, ["1", "2", "3", "4"]),
    (1234, 2, ["12", "34"]),
])
def test_split(number, split_length, expected):
    n = Number(number)
    assert n.split(split_length) == expected

@pytest.mark.parametrize("number,expected", [
    (1, False),
    (11, True),
    (12, False),
    (111, True),
    (112, False),
    (1212, True),
    (1213, False),
    (123123, True),
    (123123123, True),
    (12312312, False),
])
def test_is_invalid_id(number, expected):
    n = Number(number)
    assert n.is_invalid_id() == expected

