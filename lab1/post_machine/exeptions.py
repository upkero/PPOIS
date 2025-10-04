class ProgramParseError(Exception):
    pass


class MachineHalt(Exception):
    """Raised when HALT is executed (optional use)."""