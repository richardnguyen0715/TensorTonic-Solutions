import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here

    if not vocab:
        return np.array([], dtype=int)
    
    output = {key: 0 for key in vocab}

    for token in tokens:
        if token in vocab:
            output[token] += 1

    return np.array(list(output.values()))