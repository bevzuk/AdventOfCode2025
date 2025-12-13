from src.number import Number


class InvalidId:
    def __init__(self, value):
        self._value = self._create_invalid_id(value)

    def value(self) -> int:
        return self._value

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
