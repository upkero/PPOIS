class BedUnavailableException(Exception):
    """Raised when no beds are available for allocation."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
