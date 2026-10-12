def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    """
    Returns the weighted rating for every item.
    """
    # Write code here
    n = len(items)
    ans = []
    for avg_rating, vote_count in items:
        deter = vote_count + min_votes
        ans.append((avg_rating * vote_count / deter) + (global_mean * min_votes / deter))
    return ans