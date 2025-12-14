class Range:
    """Represents a numeric range with start and end boundaries."""

    def __init__(self, start: int, end: int):
        """Initialize Range with start and end boundaries.

        Args:
            start: The start boundary of the range
            end: The end boundary of the range
        """
        self.start = start
        self.end = end

    def contains(self, value) -> bool:
        """Check if a value is within the range boundaries (inclusive).

        Args:
            value: The value to check (InvalidId or Number)

        Returns:
            True if value is between start and end (inclusive), False otherwise
        """
        return self.start <= value.value() <= self.end
