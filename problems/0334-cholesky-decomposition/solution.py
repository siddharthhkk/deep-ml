import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    
    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)
    
    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    # Your code here
    try:
        A = np.array(A, dtype=float)
        if not np.allclose(A, A.T): return -1
        L = np.linalg.cholesky(A)
        return [[float(x) for x in rows] for rows in L]
    except (np.linalg.LinAlgError, ValueError): return -1
    pass