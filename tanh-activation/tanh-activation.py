import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here

    x = np.asarray(x, dtype=np.float64)
    x = np.clip(x, -500, 500)

    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))