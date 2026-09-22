def double_exponential_smoothing(series: list, alpha: float, beta: float) -> list:
    """
    Returns the smoothed level at every time step.
    """
    level = series[0]
    trend = series[1] - series[0]

    result = [level]

    for t in range(1, len(series)):
        old_level = level

        # Update level
        level = alpha * series[t] + (1 - alpha) * (level + trend)

        # Update trend
        trend = beta * (level - old_level) + (1 - beta) * trend

        # Store the new level
        result.append(level)

    return result
