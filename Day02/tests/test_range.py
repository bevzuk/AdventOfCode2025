import pytest
from src.range import Range
from src.invalid_id import InvalidId


def test_range_init():
    range = Range(1, 2)
    assert range.start == 1
    assert range.end == 2


@pytest.mark.parametrize("start,end,input_number,expected", [
    (10, 20, 11, True),
    (10, 20, 22, False),
    (11, 20, 11, True),
    (10, 22, 22, True),
    (10, 21, 22, False),
])
def test_invalid_id_is_in_range(start, end, input_number, expected):
    range_obj = Range(start, end)
    invalid_id = InvalidId(input_number)
    assert range_obj.contains(invalid_id) == expected
