class InvalidTicketStatusException(Exception):
    """Raised when a ticket status change is invalid."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
