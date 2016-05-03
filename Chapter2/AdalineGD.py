class AdalineGD(object):
    """AdAptive LInear NEuron classifier.

    Parameters
    ------------
    eta: float
        Learning rate(between 0.0 and 1.0)
    n_iter: int
        Passes over the training dataset.

    Attributes
    ------------
    w_: 1d-array
        Weights after fitting
    errors_: list
    
    """
def __init__(self, eta=0.01, n_iter=50):
    self.eta = eta
    self.n_iter - n_iter

def fir(self, X, y):
    """Fit training data. 

    Parameters
    ------------
    X: {array-like}, shape = [n_samples, n_features]
       Training vectors,
       where n_samples is the number of samples and n_features is the number of features
    """