def user_based_cf_prediction(similarities: list, ratings: list) -> float:
    """
    Returns the positive-similarity weighted rating prediction.
    """
    # Write code here

    n = len(similarities)
    weightSum = 0
    posSimiSum = 0

    for i in range(n):
        if similarities[i] > 0:
            posSimiSum += similarities[i]
            weightSum += similarities[i] * ratings[i]

    return weightSum / posSimiSum if posSimiSum != 0 else 0.0
    