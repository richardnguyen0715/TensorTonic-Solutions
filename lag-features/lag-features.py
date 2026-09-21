def lag_features(series: list, lags: list) -> list:
    """
    Returns the lag feature matrix.
    """
    # Write code here
    ans = []
    n_time = len(series)
    n_lag = len(lags)
    max_lag = max(lags)
    for t in range(max_lag, n_time):
        row = []
        for lag in lags:
            row.append(series[t - lag])
        ans.append(row)
    return ans
        
            