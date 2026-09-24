import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X, dtype=float)

    # Center each feature by subtracting its mean
    X_c = X - np.mean(X, axis=0)

    # Sample covariance matrix
    N = X.shape[0]
    covariance = (X_c.T @ X_c) / (N - 1)

    return covariance