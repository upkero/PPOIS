class EquipmentMaintenanceException(Exception):
    """Raised when equipment is not operational."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
