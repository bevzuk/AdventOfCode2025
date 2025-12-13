from src.number import Number


class InvalidId:
    def __init__(self, value):
        self._value = self._create_invalid_id(value)

    def value(self) -> int:
        return self._value

    def next(self):
        return InvalidId(self.value() + 1)

    def __eq__(self, other) -> bool:
        """Compare InvalidId objects by their value."""
        if isinstance(other, InvalidId):
            return self._value == other._value
        return False

    def __hash__(self) -> int:
        """Make InvalidId hashable based on its value."""
        return hash(self._value)

    def __repr__(self) -> str:
        """String representation of InvalidId."""
        return f"InvalidId({self._value})"

    def _create_invalid_id(self, value) -> int:
        number = Number(value)
        left = number.left()
        right = number.right()

        if not number.is_power_even():
            return 10 ** number.power() + 10 ** (number.power_half() - 1)

        if left == right:
            return value

        if left > right:
            return left * 10 ** number.power_half() + left

        if left < right:
            left += 1
            return left * 10 ** number.power_half() + left
