import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """
    X = X[batch_indices]
    y = y[batch_indices]
    m = len(batch_indices)
    pred = np.dot(X, weights) + bias
    errors = pred - y
    gradw = (2 / m) * np.dot(X.T, errors)
    gradb = (2 / m) * np.sum(errors)
    w = weights - lr * gradw
    b = bias - lr * gradb
    return np.append(w, b)
    pass
