import math
import numpy as np

def evaluate_shadow(production_log: list, shadow_log: list, criteria: dict) -> dict:
    """
    Returns a dictionary with the promotion decision and metrics.
    """
    # Write code here
    ipid = "input_id"
    pred = "prediction"
    act =  "actual"
    late =  "latency_ms"

    n = len(production_log)

    production_acc = 0
    shadow_acc = 0
    production_latency = []
    shadow_latency = []
    aggrement_pos = 0

    for request_idx in range(n):
        production = production_log[request_idx]
        shadow = shadow_log[request_idx]

        if production[pred] == production[act]:
            production_acc += 1

        if shadow[pred] == shadow[act]:
            shadow_acc += 1

        if production[pred] == shadow[pred]:
            aggrement_pos += 1

        production_latency.append(production[late])
        shadow_latency.append(shadow[late])

    production_acc /= n
    shadow_acc /= n
    
    gain_acc = shadow_acc - production_acc
    aggrement_rate = aggrement_pos / n
    
    sorted_latencies = sorted(shadow_latency)
    n = len(sorted_latencies)
    
    p95_index = math.ceil(0.95 * n) - 1
    
    p95_latency = sorted_latencies[p95_index]

    is_promote = False
    if gain_acc >= criteria['min_accuracy_gain'] and aggrement_rate >= criteria['min_agreement_rate'] and p95_latency <= criteria['max_latency_p95']:
        is_promote = True

    ans = {
        "promote": is_promote,
        "metrics": {
            "shadow_accuracy": shadow_acc,
            "production_accuracy": production_acc,
            "accuracy_gain": gain_acc,
            "shadow_latency_p95": p95_latency,
            "agreement_rate": aggrement_rate
        }
    }

    print(ans)

    return ans
    

        
        