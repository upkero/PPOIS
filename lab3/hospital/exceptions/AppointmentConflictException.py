class AppointmentConflictException(Exception):
    """Raised when an appointment conflicts with existing schedule."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
