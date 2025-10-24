class PaymentDeclinedException(Exception):
    """Raised when a payment does not meet requirements."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
