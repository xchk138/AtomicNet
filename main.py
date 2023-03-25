# main.py
# a simple demo to run AtomicNet to classify digits.
from model import AtomicNet


# coroutine of predictor
def CoroPredictor(model_path):
    # loading the network with weights
    model = AtomicNet(weighted_graph = model_path)
    # check if model is good

    # run a empty vector of input to reset network

    # switch to another coroutine 


def DemoAtomicNet(input_image_path):
    pass
    


if __name__ == '__main__':
    