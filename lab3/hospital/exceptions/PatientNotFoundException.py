class PatientNotFoundException(Exception):
    """Raised when patient data cannot be located."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
