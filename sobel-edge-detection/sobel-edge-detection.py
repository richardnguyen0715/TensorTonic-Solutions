import math

def sobel_edges(image: list) -> list:
    """
    Returns the zero-padded Sobel gradient magnitude at every pixel.
    """
    G_x = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    G_y = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]

    n_image = len(image)
    m_image = len(image[0])

    # Step 1: Zero padding
    padded = [
        [0] * (m_image + 2)
        for _ in range(n_image + 2)
    ]

    for i in range(n_image):
        for j in range(m_image):
            padded[i + 1][j + 1] = image[i][j]

    # Step 2 & 3: Convolution
    result = [
        [0] * m_image
        for _ in range(n_image)
    ]

    for i in range(n_image):
        for j in range(m_image):

            gx = 0
            gy = 0

            # Apply 3x3 kernel
            for ki in range(3):
                for kj in range(3):
                    pixel = padded[i + ki][j + kj]

                    gx += pixel * G_x[ki][kj]
                    gy += pixel * G_y[ki][kj]

            # Step 4: Gradient magnitude
            magnitude = math.sqrt(gx ** 2 + gy ** 2)

            result[i][j] = magnitude

    return result