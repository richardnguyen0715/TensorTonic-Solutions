import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.array(x, dtype=np.float64)
    # vectorize trả về một hàm
    erf_vectorized = np.vectorize(lambda t: math.erf(t / math.sqrt(2)))
    return 0.5 * x * (1 + erf_vectorized(x))
