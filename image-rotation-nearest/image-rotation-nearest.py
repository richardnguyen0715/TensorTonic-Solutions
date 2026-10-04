import math

def rotate_image(image: list, angle_degrees: float) -> list:
    """
    Returns the counterclockwise nearest-neighbor rotation.
    """
    H = len(image)
    W = len(image[0])

    # Center
    cy = (H - 1) / 2
    cx = (W - 1) / 2

    # Degrees -> radians
    theta = angle_degrees * math.pi / 180

    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    # Output image
    result = [[0] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            # Position relative to center
            dy = i - cy
            dx = j - cx

            # Inverse rotation
            sy = cy + dy * cos_theta + dx * sin_theta
            sx = cx - dy * sin_theta + dx * cos_theta

            # Nearest-neighbor
            sy = round(sy)
            sx = round(sx)

            # Check bounds
            if 0 <= sy < H and 0 <= sx < W:
                result[i][j] = image[sy][sx]

    return result