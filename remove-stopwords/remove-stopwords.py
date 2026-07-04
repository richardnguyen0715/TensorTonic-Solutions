def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    setStopWords = set(stopwords)
    ans = []
    for word in tokens:
        if word not in setStopWords:
            ans.append(word)
    return ans
    