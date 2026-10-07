def item_cf_predict(
    user_ratings: list,
    item_similarities: list,
    target: int
) -> float:
    numerator = 0.0
    denominator = 0.0

    for i in range(len(user_ratings)):
        # Skip the target item
        if i == target:
            continue

        rating = user_ratings[i]
        similarity = item_similarities[i]

        # Only use positive rating AND positive similarity
        if rating > 0 and similarity > 0:
            numerator += similarity * rating
            denominator += similarity

    # No qualifying items
    if denominator == 0:
        return 0.0

    return numerator / denominator