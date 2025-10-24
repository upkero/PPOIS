class MedicationOutOfStockException(Exception):
    """Raised when a medication cannot be dispensed."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
