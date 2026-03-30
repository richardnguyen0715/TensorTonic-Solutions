import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Convert to numpy arrays
    anchor = np.array(anchor)
    positive = np.array(positive)
    negative = np.array(negative)
    
    if anchor.ndim == 1:
        anchor = anchor.reshape(1, -1)
        positive = positive.reshape(1, -1)
        negative = negative.reshape(1, -1)

    p_distance = np.sum((anchor - positive) ** 2, axis=1)
    n_distance = np.sum((anchor - negative) ** 2, axis=1)

    print(p_distance)
    print(n_distance)

    losses = np.maximum(0, p_distance - n_distance + margin)

    print(losses)

    return np.mean(losses)