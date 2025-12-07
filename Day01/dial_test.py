import pytest
from dial import Dial


def test_default_is_50():
    dial = Dial()
    assert dial.get_position() == 50
    assert dial.get_zeros_count() == 0

def test_50_r10_is_60():
    dial = Dial()
    dial.rotate('R', 10)
    assert dial.get_position() == 60

def test_50_l10_is_40():
    dial = Dial()
    dial.rotate('L', 10)
    assert dial.get_position() == 40

def test_50_r50_is_0():
    dial = Dial()
    dial.rotate('R', 50)
    assert dial.get_position() == 0

def test_50_l51_is_99():
    dial = Dial()
    dial.rotate('L', 51)
    assert dial.get_position() == 99

@pytest.mark.parametrize("direction,distance,expected_zero_count", [
    ('R', 49, 0),       # 50 + 49 = 99, crosses 0 never
    ('L', 49, 0),       # 50 - 49 = 1, crosses 0 never
    ('R', 50, 1),       # 50 + 50 = 100, crosses 0 once
    ('R', 51, 1),       # 50 + 51 = 101, crosses 0 once
    ('L', 50, 1),       # 50 - 50 = 0, crosses 0 once
    ('L', 51, 1),       # 50 - 51 = -1, crosses 0 once
    ('R', 100, 1),      # 50 + 100 = 150, crosses 0 once
    ('R', 150, 2),      # 50 + 150 = 200, crosses 0 twice
    ('R', 200, 2),      # 50 + 200 = 250, crosses 0 twice
    ('L', 100, 1),      # 50 - 100 = -50, crosses 0 once
    ('L', 150, 2),      # 50 - 150 = -100, crosses 0 twice
    ('L', 200, 2),      # 50 - 200 = -150, crosses 0 twice
    ('R', 1000, 10),    # 50 + 1000 = 1050, crosses 0 ten times
    ('L', 1000, 10),    # 50 - 1000 = -950, crosses 0 ten times
])
def test_zeros_count_calculates_crossing_0(direction, distance, expected_zero_count):
    dial = Dial()
    dial.rotate(direction, distance)
    assert dial.get_zeros_count() == expected_zero_count

@pytest.mark.parametrize("start_position,direction,distance,expected_zero_count", [
    (0, 'R', 1, 0),
    (0, 'R', 99, 0),
    (99, 'R', 1, 1),
    (0, 'L', 1, 0),
    (0, 'L', 99, 0),
    (0, 'L', 100, 1),
    (0, 'L', 1000, 10),
    (1, 'L', 1, 1),
])
def test_zeros_count_calculates_crossing_0_from_start_position(start_position, direction, distance, expected_zero_count):
    dial = Dial(start_position)
    dial.rotate(direction, distance)
    assert dial.get_zeros_count() == expected_zero_count
