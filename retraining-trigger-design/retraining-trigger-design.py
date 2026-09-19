def retraining_policy(daily_stats: list, config: dict) -> list:
    """
    Returns a list of retraining day numbers.
    """
    budget = config["budget"]
    retrain_cost = config["retrain_cost"]

    last_retrain_day = -config["cooldown"]  # initial cooldown is satisfied
    days_since_retrain = 0

    ans = []

    for stat in daily_stats:
        day = stat["day"]

        # Must increment BEFORE checking today's conditions
        days_since_retrain += 1

        # Does today request retraining?
        request_retrain = (
            stat["drift_score"] > config["drift_threshold"]
            or stat["performance"] < config["performance_threshold"]
            or days_since_retrain >= config["max_staleness"]
        )

        # Can we actually retrain?
        cooldown_ok = (
            day - last_retrain_day >= config["cooldown"]
        )

        budget_ok = budget >= retrain_cost

        if request_retrain and cooldown_ok and budget_ok:
            budget -= retrain_cost
            ans.append(day)

            last_retrain_day = day
            days_since_retrain = 0

    return ans