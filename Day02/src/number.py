class Number:
    def __init__(self, value: int):
        self._value = value

    def value(self) -> int:
        return self._value

    def power(self) -> int:
        if self._value == 0:
            return 0

        power = 1
        number = self._value
        while number // 10 > 0:
            power += 1
            number //= 10

        return power

    def is_power_even(self) -> bool:
        return self.power() % 2 == 0

    def power_even(self) -> int:
        power = self.power()
        if not self.is_power_even():
            power += 1
        return power
    
    def power_half(self) -> int:
        return self.power_even() // 2

    def right(self) -> int:
        return self._value % 10 ** self.power_half()
    
    def left(self) -> int:
        return (self._value - self.right()) // 10 ** self.power_half()
    
    def split(self, interval_length):
        string_value = str(self.value())
        result = [string_value[i:i+interval_length] for i in range(0, len(string_value), interval_length)]
        return result

    
    def is_invalid_id(self) -> bool:
        if self.value() <= 10:
            return False
        
        for length in range(1, self.power_half() + 1):
            parts = self.split(length)
            if len(set(parts)) == 1:
                return True

        return False
    
    def next(self):
        return Number(self.value() + 1)