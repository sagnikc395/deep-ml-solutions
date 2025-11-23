import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    arr = np.array(X)
    mean = np.mean(arr,axis=axis,keepdims=True)
    std = np.std(arr,axis=axis,keepdims=True)

    z_score = (arr - mean) / np.maximum(std,eps)
    return z_score    
