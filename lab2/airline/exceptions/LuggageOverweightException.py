class LuggageOverweightException(Exception):
    """Raised when luggage exceeds the permitted weight."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
