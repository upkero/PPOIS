from enum import Enum, auto


class Op(Enum):
    MARK = auto()   # write '1'
    ERASE = auto()  # write '_'
    R = auto()
    L = auto()
    JZ = auto()     # jump if current == '_'
    JNZ = auto()    # jump if current != '_'
    GOTO = auto()
    HALT = auto()