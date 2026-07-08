import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    if not max_len:
        n = float("-inf")
        for seq in seqs:
            n = max(n, len(seq))
    else:
        n = max_len

    ans = []
    for seq in seqs:
        if len(seq) < n:
            temp = [pad_value] * (n - len(seq))
            seq.extend(temp)
        else:
            seq = seq[:n]
        ans.append(seq)

    return ans