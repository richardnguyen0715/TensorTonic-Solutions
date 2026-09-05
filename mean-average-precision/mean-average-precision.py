import numpy as np

def mean_average_precision(y_true_list: list, y_score_list: list, k: int | None = None) -> dict:
    """
    Returns a dictionary with map_value and ap_per_query.
    """
    # Write code here
    n = len(y_true_list)
    
    APs = []
    mAP = 0

    # Queries loop
    for idx in range(n):

        y_score_i = y_score_list[idx]
        y_true_i = y_true_list[idx]

        print(y_score_i)
        print(y_true_i)

        m = len(y_score_i)
        cutoff = k if k != None else m

        # Sort the score with true
        paired = list(zip(y_score_i, y_true_i))
        print(paired)
    
        paired.sort(reverse=True)
        
        y_score_i_sorted = [x[0] for x in paired]
        y_true_i_sorted = [x[1] for x in paired]
        print("Done Sort")
        
        # Compute R & Count 1 @ Rank
        R = 0
        CountAtRank = [0] * m
        if y_true_i_sorted[0] == 1:
            R += 1
            CountAtRank[0] = 1
        for i in range(1, m):
            if y_true_i_sorted[i] == 1:
                R += 1
                CountAtRank[i] = CountAtRank[i-1] + 1
            else:
                CountAtRank[i] = CountAtRank[i-1]
        print("R: ", R)
        print("Count At Rank: ", CountAtRank)
        print("Done Compute")

        # Compute Precision @ Rank
        PreAtRank = CountAtRank.copy()
        for i in range(m):
            PreAtRank[i] /= (i + 1)
        print("Pre At Rank: ", PreAtRank)
        print("Done Pre")
        
        # Compute AP @ cutoff
        AP = 0
        for i in range(cutoff):
            AP += PreAtRank[i] * y_true_i_sorted[i]
        print("Sum AP: ", AP)
        print("Done AP")

        # Devide by R if R > 0
        if R > 0:
            AP /= R

        APs.append(AP)

        print("-----")
                 
    mAP = np.mean(APs)

    return {"map_value": mAP, "ap_per_query": APs}