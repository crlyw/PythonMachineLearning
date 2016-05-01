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
