class FlightCancelledException(Exception):
    """Raised when an operation targets a cancelled flight."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
