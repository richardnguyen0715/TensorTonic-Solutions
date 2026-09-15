import statistics
import math

def adjusted_cosine_similarity(ratings_matrix: list, item_i: int, item_j: int) -> float:
    """
    Returns the adjusted cosine similarity between the requested items.
    """
    # Write code here

    n = len(ratings_matrix)
    r_mean = []
    for user in ratings_matrix:
        user_mean = 0
        nonZero_count = 0
        for rating in user:
            if rating != 0:
                nonZero_count += 1
                user_mean += rating
        if nonZero_count != 0:
            r_mean.append(user_mean / nonZero_count)

    print(r_mean)
    
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0

    for idx, user in enumerate(ratings_matrix):

        if user[item_i] != 0 and user[item_j] != 0:
            sum_1 += (user[item_i] - r_mean[idx]) * (user[item_j] - r_mean[idx])
            sum_2 += (user[item_i] - r_mean[idx]) ** 2
            sum_3 += (user[item_j] - r_mean[idx]) ** 2

    print(sum_1)
    print(sum_2)
    print(sum_3)
    
    return sum_1 / (math.sqrt(sum_2) * math.sqrt(sum_3)) if sum_2 != 0 and sum_3 != 0 else 0.0