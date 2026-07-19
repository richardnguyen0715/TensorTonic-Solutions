import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here


    x = np.array(x, dtype=np.float64)
    
    if rng is None:
        random = np.random.random(x.shape)
    else:
        random = rng.random(x.shape)

    mask = (random > p).astype(np.float64)

    scale = 1 / (1 - p)
    scale = mask * scale

    output = x * scale

    return output, scale

    