def bilinear_resize(image: list, new_h: int, new_w: int) -> list:
    """
    Returns a two-dimensional list with shape (new_h, new_w).
    """
    # Write code here

    n_row = len(image)
    n_col = len(image[0])
    ans = []

    for row in range(new_h):
        y = row * ((n_row - 1) / (new_h - 1)) if new_h != 1 else 0
        y0 = int(y)
        dy = y - y0
        y1 = y0 + 1 if y0 + 1 < n_row else y0
        new_row = []
        for col in range(new_w):
            x = col * ((n_col - 1) / (new_w - 1)) if new_w != 1 else 0
            x0 = int(x)
            dx = x - x0
            x1 = x0 + 1 if x0 + 1 < n_col else x0

            v0 = image[y0][x0] * (1 - dx) + image[y0][x1] * dx
            v1 = image[y1][x0] * (1 - dx) + image[y1][x1] * dx

            oij = v0 * (1 - dy) + v1 * dy
            
            new_row.append(oij)
        ans.append(new_row)
    return ans
            
            
            