class CateringItemMissingException(Exception):
    """Raised when a catering order lacks items."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
