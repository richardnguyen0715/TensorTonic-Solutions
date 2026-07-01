from collections import defaultdict

def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here

    ans = defaultdict(int)

    for sentence in sentences:
        for word in sentence:
            ans[word] += 1

    return ans