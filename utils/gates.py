# gates.py
import torch
import torch.nn as nn
import numpy as np

GATE_NOT = 0
GATE_AND = 1

class NotGate(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.type_id = GATE_NOT
    def __str__(self) -> str:
        return 'Logic Gate [NOT]'
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return 1 - x
    def validate(self, x: torch.Tensor) -> bool:
        x_raw = x.detach().cpu().numpy()
        if np.any(x_raw < 0) or np.any(x_raw > 1.0):
            print('Gate [NOT] cannot process input :' + str(x_raw))
            return False
        else:
            return True


class AndGate(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.type_id = GATE_AND
    def __str__(self) -> str:
        return 'Logic Gate [AND]'
    def forward(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
        return x1*x2
    def validate(self, x1: torch.Tensor, x2: torch.Tensor) -> bool:
        x_raw = x1.detach().cpu().numpy()
        if np.any(x_raw < 0) or np.any(x_raw > 1.0):
            print('Gate [AND] cannot process input #1:' + str(x_raw))
            return False
        else:    
            x_raw = x2.detach().cpu().numpy()
            if np.any(x_raw < 0) or np.any(x_raw > 1.0):
                print('Gate [AND] cannot process input #2:' + str(x_raw))
                return False
            else:
                return True

class LogicGate(nn.Module):
    def __init__(self, type:int) -> None:
        super().__init__()
        self.type = type
        self.gate = None
        if self.type == GATE_NOT:
            self.gate = NotGate()
        elif type == GATE_AND:
            self.gate = AndGate()
        else:
            raise TypeError("undefined logic type id: %d" % type)
    def forward(self, x1:torch.Tensor, x2:torch.Tensor=None)-> torch.Tensor:
        if self.type == GATE_NOT:
            return self.gate(x1)
        elif self.type == GATE_AND:
            return self.gate(x1, x2)
    def __str__(self) -> str:
        return 'Logic Gate\n' + super().__str__()
    
