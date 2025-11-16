#https://www.tensortonic.com/problems/cosine-similarity

import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    arr_a = np.array(a)
    arr_b = np.array(b)

    norm_a = np.linalg.norm(arr_a)
    norm_b = np.linalg.norm(arr_b)

    if norm_a == 0 or norm_b == 0:
        return 0
    return np.dot(arr_a,arr_b) / (norm_a * norm_b)
