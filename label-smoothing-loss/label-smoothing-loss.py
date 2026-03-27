def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    k = len(predictions)
    qi = [(1 - epsilon) + epsilon / k if i == target else epsilon / k for i in range(k)]
    labelLoss = 0
    for i in range(k):
        labelLoss += -1* (qi[i] * math.log(predictions[i]))

    return labelLoss