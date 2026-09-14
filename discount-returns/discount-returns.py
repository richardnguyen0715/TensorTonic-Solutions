def discount_returns(rewards: list, gamma: float) -> list:
    """
    Returns the discounted return at every timestep.
    """
    # Write code here
    n = len(rewards)
    ans = [0] * n

    def recur(t):
        if t == n - 1:
            ans[t] = rewards[t]
            return ans[t]

        ans[t] = rewards[t] + gamma * recur(t + 1)
        return ans[t]

    if n > 0:
        recur(0)

    return ans
        