import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the Pearson correlation matrix as a NumPy array.
    """
    n_sample = len(X)
    n_feature = len(X[0])

    # Get features as NumPy arrays
    features = np.array(X, dtype=float).T

    # Step 1: Means
    features_mean = np.mean(features, axis=1)

    # Step 2: Deviations from the mean
    features_deviation = features - features_mean[:, np.newaxis]

    # Step 3: Sample covariance matrix
    covariance = np.zeros((n_feature, n_feature))

    for i in range(n_feature):
        for j in range(n_feature):
            covariance[i, j] = (
                np.sum(
                    features_deviation[i] * features_deviation[j]
                ) / (n_sample - 1)
            )

    # Step 4: Standard deviations
    std = np.sqrt(np.diag(covariance))

    # Step 5: Correlation matrix
    correlation = np.full((n_feature, n_feature), np.nan)

    for i in range(n_feature):
        for j in range(n_feature):
            if std[i] != 0 and std[j] != 0:
                correlation[i, j] = covariance[i, j] / (std[i] * std[j])

    return correlation