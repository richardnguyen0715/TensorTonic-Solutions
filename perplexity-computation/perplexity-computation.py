def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    n = len(prob_distributions)
    h = 0
    
    for i in range(n):
        p = prob_distributions[i][actual_tokens[i]]
        logP = math.log(p)
        h += logP

    h *= -1
    h /= n

    return math.exp(h)