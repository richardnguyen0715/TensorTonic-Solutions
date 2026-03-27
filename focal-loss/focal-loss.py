import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.array(p, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    fl = -1 * (1 - p) ** gamma * y * np.log(p) - p ** gamma * (1 - y) * np.log(1 - p)

    return np.mean(fl)