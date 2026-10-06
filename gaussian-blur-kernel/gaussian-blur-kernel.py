import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    center = size // 2
    kernel = []
    total = 0.0

    # Compute unnormalized Gaussian weights
    for y in range(size):
        row = []
        for x in range(size):
            dx = x - center
            dy = y - center
            weight = math.exp(-(dx * dx + dy * dy) / (2 * sigma * sigma))
            row.append(weight)
            total += weight
        kernel.append(row)

    # Normalize so all weights sum to 1
    for y in range(size):
        for x in range(size):
            kernel[y][x] /= total

    return kernel