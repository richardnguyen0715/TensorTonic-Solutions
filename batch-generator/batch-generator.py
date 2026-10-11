import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    X = np.asarray(X)
    y = np.asarray(y)

    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    if len(X) != len(y):
        raise ValueError("X and y must have the same length")

    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(X))

    X = X[indices]
    y = y[indices]

    for start in range(0, len(X), batch_size):
        end = start + batch_size

        if drop_last and end > len(X):
            break

        yield X[start:end], y[start:end]