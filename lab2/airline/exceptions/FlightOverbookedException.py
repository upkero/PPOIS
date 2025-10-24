class FlightOverbookedException(Exception):
    """Raised when a flight receives more passengers than capacity."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
