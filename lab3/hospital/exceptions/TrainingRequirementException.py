class TrainingRequirementException(Exception):
    """Raised when staff lack required training."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
