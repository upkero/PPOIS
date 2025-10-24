class InfectionControlBreachException(Exception):
    """Raised when sanitation standards are not met."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
