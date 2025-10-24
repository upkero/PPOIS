class SecurityAlertException(Exception):
    """Raised when a critical security alert is triggered."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
