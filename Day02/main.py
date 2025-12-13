from src.range import Range
from src.invalid_id import InvalidId


def parse_ranges(input_line: str) -> list[Range]:
    """Parse range definitions from input line.

    Args:
        input_line: Comma-separated range definitions (e.g., "11-22,95-115")

    Returns:
        List of Range objects
    """
    ranges = []
    for range_def in input_line.strip().split(','):
        start, end = map(int, range_def.split('-'))
        ranges.append(Range(start, end))
    return ranges


def find_invalid_ids_in_range(range_obj: Range) -> list[InvalidId]:
    """Find all invalid IDs within a range.

    An invalid ID is one that consists of a sequence repeated twice
    (e.g., 11, 22, 123123, etc.)

    Args:
        range_obj: The range to search in

    Returns:
        List of InvalidId objects found in the range
    """
    invalid_ids = []
    current_id = InvalidId(range_obj.start)

    while range_obj.contains(current_id):
        invalid_ids.append(current_id)
        current_id = current_id.next()

    return invalid_ids


def solve(input_file: str) -> int:
    """Solve the puzzle.

    Args:
        input_file: Path to input file with range definitions

    Returns:
        Sum of all invalid IDs found across all ranges
    """
    with open(input_file, 'r') as f:
        input_line = f.read()

    ranges = parse_ranges(input_line)

    all_invalid_ids = []
    for range_obj in ranges:
        invalid_ids = find_invalid_ids_in_range(range_obj)
        all_invalid_ids.extend(invalid_ids)

    # Sum all unique invalid ID values
    total = sum(invalid_id.value() for invalid_id in set(all_invalid_ids))
    return total


if __name__ == '__main__':
    result = solve('input.txt')
    print(f"Sum of all invalid IDs: {result}")
