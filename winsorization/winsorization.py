def winsorize(values: list, lower_pct: float, upper_pct: float) -> list:
    """
    Returns values clipped to the interpolated percentile bounds.
    """
    sorted_values = sorted(values)
    n = len(sorted_values)

    def percentile(p):
        k = (n - 1) * p / 100
        lower = int(k)
        upper = min(lower + 1, n - 1)
        fraction = k - lower

        return sorted_values[lower] + fraction * (
            sorted_values[upper] - sorted_values[lower]
        )

    lower_bound = percentile(lower_pct)
    upper_bound = percentile(upper_pct)

    return [
        max(lower_bound, min(value, upper_bound))
        for value in values
    ]