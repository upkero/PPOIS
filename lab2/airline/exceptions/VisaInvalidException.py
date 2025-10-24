class VisaInvalidException(Exception):
    """Raised when a visa is not valid for travel."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
