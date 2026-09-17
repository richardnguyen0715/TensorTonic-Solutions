import numpy as np

def td_value_update(V: list, s: int, r: float, s_next: int, alpha: float, gamma: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as V.
    """
    # Write code here
    n = len(V)
    ans = V.copy()
    sigma = r + gamma * V[s_next] - V[s]
    ans[s] = V[s] + alpha * sigma
    return np.array(ans)