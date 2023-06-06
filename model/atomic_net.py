import sys
sys.path.append('./')
sys.path.append('../')

from utils.gates import LogicGate, GATE_NOT, GATE_AND 
import torch
import torch.nn as nn
import numpy as np

class AtomicNet(object):
    def __init__(self, layers):
        self.layers = []
        for i in range(len(layers)):
            num_units = layers[i]
            # for each unit in this layer, perform not or and
            self.layers += []



if __name__ == '__main__':
    print('unit test for atomic net')
    # test gate not
    gate_not = LogicGate(GATE_NOT)
    print(gate_not)
    x1 = torch.from_numpy(np.float32(np.random.rand(3,3)>0.5))
    print(x1)
    x2 = torch.from_numpy(np.float32(np.random.rand(3,3)>0.5))
    print(x2)
    y1 = gate_not(x1)
    print(y1)
    # test gate and
    gate_and = LogicGate(GATE_AND)
    print(gate_and)
    y2 = gate_and(y1, x2)
    print(y2)
    # test training such a simple demo of logic net
    opt = torch.optim.SGD(gate_and.parameters)
    