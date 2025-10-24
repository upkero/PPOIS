class LabResultDelayException(Exception):
    """Raised when a lab result is delayed."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
