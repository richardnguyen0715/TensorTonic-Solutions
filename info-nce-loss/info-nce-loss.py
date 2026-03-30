import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here

    Z2 = np.array(Z2, dtype=np.float64)
    Z1 = np.array(Z1, dtype=np.float64)

    s = np.dot(Z1, Z2.T) / temperature
    s_stable = s - np.max(s, axis=1, keepdims=True)
    exp_s = np.exp(s_stable)

    pos_pairs = np.diag(exp_s)

    sum_exp = np.sum(exp_s, axis=1)

    loss = -np.mean(np.log(pos_pairs / sum_exp))

    return loss