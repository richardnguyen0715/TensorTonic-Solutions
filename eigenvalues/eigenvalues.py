import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix and sort them
    by real part, then imaginary part.
    """
    try:
        matrix = np.asarray(matrix, dtype=np.float64)
    except:
        return None
    
    # Must be 2D
    if matrix.ndim != 2:
        return None
    
    # Must be square
    if matrix.shape[0] != matrix.shape[1]:
        return None
    
    eigenvalues = np.linalg.eigvals(matrix)
    
    eigvals_sorted = sorted(
        eigenvalues,
        key=lambda z: (z.real, z.imag)
    )
    
    return np.array(eigvals_sorted)