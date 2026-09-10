def rating_normalization(matrix: list) -> list:
    """
    Returns the mean-centered user-item matrix.
    """
    ans = []

    for user in matrix:
        sumRating = 0
        countNoneZero = 0

        for item in user:
            if item != 0:
                sumRating += item
                countNoneZero += 1
        if countNoneZero != 0:
            meanRating = sumRating / countNoneZero
        else:
            meanRating = 0

        newRating = user.copy()

        for i, rating in enumerate(newRating):
            if rating != 0:
                newRating[i] = rating - meanRating

        ans.append(newRating)

    return ans