import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.array(p, dtype = np.float64)
    y = np.array(y, dtype = np.float64)
    PY = p * y
    diceP_Y = (2 * np.sum(PY) + eps ) / (np.sum(p) + np.sum(y) + eps)
    return 1 - diceP_Y