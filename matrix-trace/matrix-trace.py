import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here

    m, n = len(A), len(A[0])

    sumA = 0
    for i in range(m):
        for j in range(n):
            if i == j:
                sumA += A[i][j] 
    return sumA
            