import math

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    
    h = 0
    n = len(actual_tokens)
    for i in range(n):
        h += math.log(prob_distributions[i][actual_tokens[i]])
    
    h *= -1
    h /= n
    
    return math.exp(h)