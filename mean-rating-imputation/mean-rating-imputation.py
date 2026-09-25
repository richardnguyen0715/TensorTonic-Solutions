def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    """
    Returns a copy with missing ratings replaced by user or item means.
    """
    if not ratings_matrix:
        return []

    rows = len(ratings_matrix)
    cols = len(ratings_matrix[0])

    # Copy để không thay đổi ratings_matrix
    result = [row[:] for row in ratings_matrix]

    if mode == "user":
        # Mean của từng row
        means = []

        for row in ratings_matrix:
            nonzero = [x for x in row if x != 0]
            means.append(sum(nonzero) / len(nonzero) if nonzero else 0.0)

        # Impute các giá trị 0
        for i in range(rows):
            for j in range(cols):
                if result[i][j] == 0:
                    result[i][j] = means[i]

    elif mode == "item":
        # Mean của từng column
        means = []

        for j in range(cols):
            nonzero = [
                ratings_matrix[i][j]
                for i in range(rows)
                if ratings_matrix[i][j] != 0
            ]

            means.append(sum(nonzero) / len(nonzero) if nonzero else 0.0)

        # Impute các giá trị 0
        for i in range(rows):
            for j in range(cols):
                if result[i][j] == 0:
                    result[i][j] = means[j]

    else:
        raise ValueError("mode must be 'user' or 'item'")

    return result