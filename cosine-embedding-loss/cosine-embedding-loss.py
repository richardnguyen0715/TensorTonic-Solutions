def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here

    def cosine_similarity(v1, v2):
        # Calculate dot product
        dot_product = sum(x * y for x, y in zip(v1, v2))
        
        # Calculate magnitudes
        magnitude_v1 = math.sqrt(sum(x**2 for x in v1))
        magnitude_v2 = math.sqrt(sum(y**2 for y in v2))
        
        # Check for division by zero
        if magnitude_v1 == 0 or magnitude_v2 == 0:
            return 0.0
            
        # Calculate cosine similarity
        similarity = dot_product / (magnitude_v1 * magnitude_v2)
        return similarity

    cosAns = cosine_similarity(x1, x2)

    if label == 1:
        return 1 - cosAns

    return max(0, cosAns - margin)