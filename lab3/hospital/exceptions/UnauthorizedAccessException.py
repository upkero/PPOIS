class UnauthorizedAccessException(Exception):
    """Raised when a user attempts unauthorized access."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
