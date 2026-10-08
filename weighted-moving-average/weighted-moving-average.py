def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    n_vals = len(values)
    n_weights = len(weights)
    sum_weights = sum(weights)

    ans = []

    for i in range(n_vals - n_weights + 1):
        wma = 0
        for j in range(n_weights):
            wma += values[i + j] * weights[j]

        ans.append(wma / sum_weights)

    return ans