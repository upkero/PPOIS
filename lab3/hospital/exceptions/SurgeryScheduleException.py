class SurgeryScheduleException(Exception):
    """Raised when a problem occurs with surgery scheduling."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
