class InsuranceClaimDeniedException(Exception):
    """Raised when an insurance claim is denied."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
