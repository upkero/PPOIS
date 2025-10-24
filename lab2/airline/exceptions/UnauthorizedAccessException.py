class UnauthorizedAccessException(Exception):
    """Raised when an unauthorized access attempt occurs."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
