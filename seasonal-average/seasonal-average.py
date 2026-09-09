def seasonal_average(series: list, period: int) -> list:
    """
    Returns the average for each position in the seasonal cycle.
    """
    # Write code here

    n = len(series)
    m = n // period
    ans = []
    for sea in range(period):
        sum = 0
        # print("season: ", sea)
        for i in range(m):
            sum += series[sea + i * period]
            # print(series[sea + i * period])
        ans.append(sum / m)
    return ans