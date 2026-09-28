def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here

    n_returns = len(returns)
    wealth = [1] * n_returns

    for i in range(n_returns):
        wealth[i] = wealth[i-1] * (returns[i] + 1)

    ans = []
    for i in range(n_returns):
        ans.append(wealth[i] - 1)

    return ans
        