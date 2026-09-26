import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    matrix = np.array(X, dtype=float)
    original_ndim = matrix.ndim

    if strategy not in ("mean", "median"):
        raise ValueError("strategy must be 'mean' or 'median'")

    if matrix.ndim == 1:
        values = np.nanmedian(matrix) if strategy == "median" else np.nanmean(matrix)

        if np.isnan(values):
            values = 0.0

        matrix[np.isnan(matrix)] = values

    else:
        values = (
            np.nanmedian(matrix, axis=0)
            if strategy == "median"
            else np.nanmean(matrix, axis=0)
        )

        values = np.nan_to_num(values, nan=0.0)

        rows, cols = np.where(np.isnan(matrix))
        matrix[rows, cols] = values[cols]

    return matrix