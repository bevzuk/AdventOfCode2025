class Number:
    def __init__(self, number: int):
        self.number = number

    def power(self) -> int:
        if self.number == 0:
            return 0

        power = 1
        number = self.number
        while number // 10 > 0:
            power += 1
            number //= 10

        return power

    def power_even(self) -> int:
        power = self.power()
        if self.power() % 2 == 1:
            power += 1
        return power
    
    def power_half(self) -> int:
        return self.power_even() // 2

    def right(self) -> int:
        return self.number % 10 ** self.power_half()
    
    def left(self) -> int:
        return (self.number - self.right()) // 10 ** self.power_half()
    
