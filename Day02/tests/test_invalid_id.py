import pytest
from src.invalid_id import InvalidId

@pytest.mark.parametrize("number,expected_invalid_id_value", [
    (11, 11),
    (10, 11),
    (20, 22),
    (23, 33),
    (123000, 123123),
    (12345, 100100),
    (1188511880, 1188511885),
    (998, 1010),
    (222220, 222222),
    (222224, 223223),
    (38593856, 38593859),
])
def test_invalid_id_init(number, expected_invalid_id_value):
    n = InvalidId(number)
    assert n.value() == expected_invalid_id_value


@pytest.mark.parametrize("current_invalid_id,expected_next_invalid_id", [
    (11, 22),
    (22, 33),
    (99, 1010),
    (1010, 1111),
    (123123, 124124),
])
def test_invalid_id_next(current_invalid_id, expected_next_invalid_id):
    invalid_id = InvalidId(current_invalid_id)
    assert invalid_id.next() == InvalidId(expected_next_invalid_id)