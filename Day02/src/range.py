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
