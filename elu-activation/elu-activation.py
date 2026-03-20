def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    for idx, val in enumerate(x):
        if val <= 0:
            x[idx] = alpha * (math.exp(val) - 1)
    return x