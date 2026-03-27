def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    import numpy as np
    predictions = np.array(predictions, dtype=np.float64)
    targets = np.array(targets, dtype=np.float64)
    pt = np.where(targets == 1, predictions, 1 - predictions)
    fl = -1 * alpha * (( 1 - pt) ** gamma) * np.log(pt)
    return np.mean(fl)
    