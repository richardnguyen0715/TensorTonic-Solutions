def nms(boxes: list, scores: list, iou_threshold: float) -> list:
    """
    Returns a list of retained indices.
    """

    score_indexed = []

    for idx, score in enumerate(scores):
        score_indexed.append((score, idx))

    score_indexed.sort(key=lambda x: -x[0])

    selected = []

    # Những box hiện tại vẫn còn được xét
    remaining = set(range(len(boxes)))

    for score, idx in score_indexed:

        # Box này đã bị box trước đó suppress
        if idx not in remaining:
            continue

        boxA = boxes[idx]

        # Chọn box A
        selected.append(idx)
        remaining.remove(idx)

        # Kiểm tra các box còn lại
        for idx_2 in remaining.copy():

            boxB = boxes[idx_2]

            # Intersection
            xL = max(boxA[0], boxB[0])
            yT = max(boxA[1], boxB[1])
            xR = min(boxA[2], boxB[2])
            yB = min(boxA[3], boxB[3])

            width = max(0, xR - xL)
            height = max(0, yB - yT)

            intersection = width * height

            # Area
            areaA = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
            areaB = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

            # IoU
            iou = intersection / (areaA + areaB - intersection)

            # Quá trùng → loại
            if iou >= iou_threshold:
                remaining.remove(idx_2)

    return selected