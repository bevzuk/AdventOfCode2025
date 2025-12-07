class Dial:
    def __init__(self, start_position=50):
        self.position = start_position
        self.zeros_count = 0

    def rotate(self, direction, distance):
        increment = 0
        if self.get_position() > 0:
            increment = 1

        if direction == 'R':
            self.position += distance
        elif direction == 'L':
            self.position -= distance

        if self.position > 99:
            self.zeros_count += self.position // 100
            self.position %= 100
        elif self.position <= 0:
            self.zeros_count += increment + (-self.position) // 100
            self.position %= 100

    def get_position(self):
        return self.position

    def get_zeros_count(self):
        return self.zeros_count
