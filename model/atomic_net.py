LOGIC_NOT = 0
LOGIC_AND = 1

class LogicNode(object):
    def __init__(self, a, b=None, type=LOGIC_NOT) -> None:
        self.type = type
        self.a = a
        self.b = b
    def forward(a, b=None):
        if type==LOGIC_NOT:
            return 1-a
        else:
            return a*b

class AtomicNet(object):
    def __init__(self, layers):
        self.layers = []
        for i in range(len(layers)):
            num_units = layers[i]
            # for each unit in this layer, perform not or and
            self.layers += []