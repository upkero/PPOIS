class BillingOverdueException(Exception):
    """Raised when a billing account is overdue."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
