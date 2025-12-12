import pytest
from Day02.number import Number

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
