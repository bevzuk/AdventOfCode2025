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