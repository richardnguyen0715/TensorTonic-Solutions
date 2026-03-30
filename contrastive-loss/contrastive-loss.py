import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here

    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    if b.ndim == 1 or a.ndim == 1:
        a = a.reshape(1, -1)
        b = b.reshape(1, -1)
        y = y.reshape(1, -1)

    d = np.linalg.norm(a - b, axis=1)

    l = y * (d ** 2) + (1 - y) * np.maximum(0, margin - d) ** 2

    if reduction == "mean":
        return np.mean(l)

    return np.sum(l)
    