class MaintenanceOverdueException(Exception):
    """Raised when an aircraft needs maintenance."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
