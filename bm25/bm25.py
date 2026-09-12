import math
from collections import Counter
import numpy as np

def bm25_score(query_tokens: list[str], docs: list[list[str]], k1: float = 1.2, b: float = 0.75) -> np.ndarray:
    """
    Returns a NumPy array with one score per document.
    """
    # Write code here
    N = len(docs)
    avgdl = 0

    if N == 0 or len(query_tokens) == 0:
        return np.empty(0)
    
    for doc in docs:
        avgdl += len(doc)
    avgdl /= N

    doc_count_list = []
    for doc in docs:
        doc_count_list.append(Counter(doc))
    
    idf_list = []
    for query in query_tokens:
        df_t = 0
        for doc_counts in doc_count_list:
            if query in doc_counts.keys():
                df_t += 1
        idf_t = np.log((N - df_t + 0.5)/(df_t + 0.5) + 1)
        print("query: ", query, ", idf: ", idf_t)
        idf_list.append(idf_t)

    ans = []
    for idx, doc_counts in enumerate(doc_count_list):
        sumScore = 0
        n = len(docs[idx])
        
        for idx, val in enumerate(query_tokens):
            idf = idf_list[idx]

            sumScore += (idf * doc_counts[val] * (k1 + 1)) / (doc_counts[val] + (k1 * (1 - b + b * (n / avgdl))))
            
        ans.append(sumScore)    

    print(ans)

    return np.array(ans, dtype=np.float64)