from atomic_net.utils import logic_node
from logic_node import *

class AtomicNet(object):
    def __init__(self, layers):
        self.layers = []
        for i in range(len(layers)):
            num_units = layers[i]
            # for each unit in this layer, perform not or and
            self.layers += []