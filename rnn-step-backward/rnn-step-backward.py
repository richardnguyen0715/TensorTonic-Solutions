import numpy as np

def rnn_step_backward(dh, cache):
    """
    Returns:
        dx_t: gradient wrt input x_t      (shape: D,)
        dh_prev: gradient wrt previous h (shape: H,)
        dW: gradient wrt W               (shape: H x D)
        dU: gradient wrt U               (shape: H x H)
        db: gradient wrt bias            (shape: H,)
    """
    # Write code here
    x_t = np.array(cache[0])
    h_prev = np.array(cache[1])
    h_t = np.array(cache[2])
    W = np.array(cache[3]) # == Wxh
    U = np.array(cache[4]) # == Whh
    b = np.array(cache[5])

    dz_t = dh * ( 1 - h_t ** 2)
    dW = np.outer(dz_t, x_t.T)
    dU = np.outer(dz_t, h_prev.T)
    db = dz_t
    dx_t = W.T @ dz_t
    dh_prev = U.T @ dz_t

    return dx_t, dh_prev, dW, dU, db
