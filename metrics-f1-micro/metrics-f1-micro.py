def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    n = len(y_pred)

    TP = 0
    FP = 0
    FN = 0

    for i, j in zip(y_pred, y_true):
        if i == j:
            TP += 1
        else:
            FP += 1
            FN += 1

    denom = 2*TP + FN + FP

    return 0.0 if denom == 0.0 else (2 * TP) / denom