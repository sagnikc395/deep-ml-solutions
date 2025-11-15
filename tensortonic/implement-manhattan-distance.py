import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    arr_x = np.array(x)
    arr_y = np.array(y)

    return np.linalg.norm(arr_x - arr_y,ord=1)

