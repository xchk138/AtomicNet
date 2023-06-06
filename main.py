# main.py
# a simple demo to run AtomicNet to classify digits.
from model import AtomicNet


# coroutine of predictor
def CoroPredictor(model_path):
    # loading the network with weights
    model = AtomicNet(weighted_graph = model_path)
    # check if model is good
    if not model.ok():
        raise AssertionError('model not okay yet!')
    # prepare the dataset
    

def DemoAtomicNet(input_image_path):
    pass
    


if __name__ == '__main__':
    pass