import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    n = len(q)
    p = np.array(p, dtype=float) 
    q = np.array(q, dtype=float) 
    p = p + eps 
    q = q + eps 
    d_kl = np.sum(p * np.log(p / q)) 
    return float(d_kl)