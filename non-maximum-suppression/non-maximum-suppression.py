def nms(boxes: list, scores: list, iou_threshold: float) -> list:
    """
    Returns a list of retained indices.
    """

    score_indexed = []

    for idx, score in enumerate(scores):
        score_indexed.append((score, idx))

    score_indexed.sort(key=lambda x: -x[0])

    selected = []

    remaining = set(range(len(boxes)))

    for score, idx in score_indexed:

        if idx not in remaining:
            continue
                    
        selected.append(idx)
        remaining.remove(idx)

        boxA = boxes[idx]

        for idx_2 in remaining.copy():

            boxB = boxes[idx_2]

            xL = max(boxA[0], boxB[0])
            yT = max(boxA[1], boxB[1])
            xR = min(boxA[2], boxB[2])
            yB = min(boxA[3], boxB[3])

            A_intersection = max(0, xR - xL) * max(0, yB - yT)
            areaA = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
            areaB = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

            IoU_AB = A_intersection / (areaA + areaB - A_intersection)

            if IoU_AB >= iou_threshold:
                remaining.remove(idx_2)


    return selected