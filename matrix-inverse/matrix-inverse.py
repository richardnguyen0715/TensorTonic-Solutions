import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    try:
        res = np.linalg.inv(A)
        return res
    except:
        return None