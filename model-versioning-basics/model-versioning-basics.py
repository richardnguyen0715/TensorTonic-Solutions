from datetime import datetime


def promote_model(models: list) -> str:
    """
    Returns the promoted model name as a string.
    """
    # Compare accuracy
    acc_queue = []
    max_acc = float("-inf")

    for model in models:
        if model["accuracy"] >= max_acc:
            acc_queue.append(model)
            max_acc = model["accuracy"]

    # Compare latency
    late_queue = []
    min_late = float("inf")

    for model in acc_queue:
        if model["latency"] <= min_late:
            min_late = model["latency"]
            late_queue.append(model)

    # Compare timestamp
    ans = None
    max_date = datetime.fromisoformat("1990-01-01")

    for model in late_queue:
        timestamp = model["timestamp"]

        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)

        if timestamp > max_date:
            ans = model
            max_date = timestamp

    return ans["name"] if ans else ""