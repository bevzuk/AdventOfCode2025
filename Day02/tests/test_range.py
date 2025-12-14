import pytest
from src.range import Range
from src.invalid_id import InvalidId
from src.number import Number


def test_range_init():
    range = Range(1, 2)
    assert range.start == 1
    assert range.end == 2

@pytest.mark.parametrize("start,end,invalid_id,expected", [
    (10, 20, 11, True),
    (10, 20, 22, False),
    (11, 20, 11, True),
    (10, 22, 22, True),
    (10, 21, 22, False),
])
def test_invalid_id_is_in_range(start, end, invalid_id, expected):
    range_obj = Range(start, end)
    invalid_id = InvalidId(invalid_id)
    assert range_obj.contains(invalid_id) == expected

@pytest.mark.parametrize("start,end,number_value,expected", [
    (10, 20, 11, True),
    (10, 20, 22, False),
    (11, 20, 11, True),
    (10, 22, 22, True),
    (10, 21, 22, False),
])
def test_number_is_in_range(start, end, number_value, expected):
    range_obj = Range(start, end)
    number = Number(number_value)
    assert range_obj.contains(number) == expected
