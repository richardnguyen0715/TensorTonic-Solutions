def catalog_coverage(recommendations: list, n_items: int) -> float:
    """
    Returns the fraction of catalog items that were recommended.
    """
    # Write code here
    if n_items == 0.0:
        return 0.0

    appearCount = 0
    visited = set()

    
    for user in recommendations:
        for item in user:
            if item not in visited:
                appearCount += 1
                visited.add(item)

    return appearCount / n_items
    