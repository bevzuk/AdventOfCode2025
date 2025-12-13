import pytest
from src.range import Range


def test_range_init():
    range = Range(1, 2)
    assert range.start == 1
    assert range.end == 2
