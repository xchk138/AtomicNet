import torch
import torch.nn as nn

class GateType(object):
    def __init__(self) -> None:
        raise TypeError('interface instead of class being used!')
    def __str__(self) -> str:
        return 'GateType'

class NotGate(GateType):
    def __init__(self) -> None:
        super().__init__()
        self.type_id = 0
    def __str__(self) -> str:
        return 'Logic Gate [NOT]'

class AndGate(GateType):
    def __init__(self) -> None:
        super().__init__()
        self.type_id = 1
    def __str__(self) -> str:
        return 'Logic Gate [AND]'


class LogicGate(torch.):
    def __init__(self, type:GateType) -> None:
        self.type = type
    def forward(self, a, b=None):
        if type==LOGIC_NOT:
            return 1-a
        elif type==LOGIC_AND:
            return a*b
        else:
            raise TypeError("undefined logic node type: %d" % type)
    def dump()
