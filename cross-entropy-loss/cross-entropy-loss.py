import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_true = np.array(y_true, dtype=np.int64)
    y_pred = np.array(y_pred, dtype=np.float64)

    p_true = y_pred[np.arange(len(y_true)), y_true]
    losses = -np.log(p_true)
    return np.mean(losses)