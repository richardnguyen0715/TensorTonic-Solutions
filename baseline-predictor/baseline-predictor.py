def baseline_predict(ratings_matrix: list, target_pairs: list) -> list:
    """
    Returns the baseline predictions for the requested user-item pairs.
    """
    n_users = len(ratings_matrix)
    n_items = len(ratings_matrix[0]) if n_users else 0

    # Global mean
    total = 0
    count = 0

    # User sums/counts
    user_sum = [0] * n_users
    user_count = [0] * n_users

    # Item sums/counts
    item_sum = [0] * n_items
    item_count = [0] * n_items

    for u in range(n_users):
        for i in range(n_items):
            rating = ratings_matrix[u][i]

            # 0 means "not observed"
            if rating != 0:
                total += rating
                count += 1

                user_sum[u] += rating
                user_count[u] += 1

                item_sum[i] += rating
                item_count[i] += 1

    mu = total / count

    # Biases
    user_bias = [0] * n_users
    item_bias = [0] * n_items

    for u in range(n_users):
        if user_count[u] > 0:
            user_mean = user_sum[u] / user_count[u]
            user_bias[u] = user_mean - mu

    for i in range(n_items):
        if item_count[i] > 0:
            item_mean = item_sum[i] / item_count[i]
            item_bias[i] = item_mean - mu

    # Predictions
    predictions = []

    for u, i in target_pairs:
        prediction = mu + user_bias[u] + item_bias[i]
        predictions.append(prediction)

    return predictions