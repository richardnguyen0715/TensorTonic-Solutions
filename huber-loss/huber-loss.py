import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here

    y_pred = np.array(y_pred, dtype=np.float64)
    y_true = np.array(y_true, dtype=np.float64)

    e = y_true - y_pred

    loss = np.where(np.abs(e) > delta, delta * (np.abs(e) - 0.5 * delta), 0.5 * e * e)
    return np.mean(loss)