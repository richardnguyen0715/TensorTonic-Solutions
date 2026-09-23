def autocorrelation(series: list, max_lag: int) -> list:
    """
    Returns normalized autocorrelation from lag zero through max_lag.
    """
    # Write code here

    x_mean = 0
    n_series = len(series)
    for point in series:
        x_mean += point
    x_mean /= n_series if n_series != 0 else 0
    y_variance = 0

    for point in series:
        y_variance += (point - x_mean) ** 2

    if y_variance == 0:
        return [1.0] + [0.0] * max_lag

    ans = [1.0]

    for lag in range(1, max_lag + 1):
        r_k = 0

        for idx in range(n_series - lag):
            r_k += (
                (series[idx] - x_mean)
                * (series[idx + lag] - x_mean)
            )

        r_k /= y_variance
        ans.append(r_k)

    return ans
        