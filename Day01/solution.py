from dial import Dial


def main():
    dial = Dial()

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            dial.rotate(direction, distance)

    print(dial.get_zeros_count())


if __name__ == '__main__':
    main()
