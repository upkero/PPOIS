class SeatAlreadyAssignedException(Exception):
    """Raised when trying to reassign a reserved seat."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
