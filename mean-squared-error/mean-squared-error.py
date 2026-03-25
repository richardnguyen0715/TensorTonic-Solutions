import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here

    y_pred = np.array(y_pred, dtype=np.float64)
    y_true = np.array(y_true, dtype=np.float64)

    minus = y_pred - y_true
    squared = minus * minus
    sum = np.sum(squared)
    return 1 / len(minus) * sum    
    