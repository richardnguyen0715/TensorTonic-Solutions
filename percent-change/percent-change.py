def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    # Write code here

    ans = []
    n = len(series)
    for i in range(1, n):
        if series[i - 1] != 0:
            ans.append((series[i] - series[i - 1])/ series[i - 1])
        else:
            ans.append(float(0))
    return ans