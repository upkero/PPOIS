class LoyaltyTierUpgradeException(Exception):
    """Raised when a loyalty tier upgrade cannot proceed."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
