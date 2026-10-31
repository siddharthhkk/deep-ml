import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    m, n = X.shape
    for i in range(n_iter):
        j = i % m
        pred = np.dot(X[j], weights)
        error = pred - y[j]
        grad = 2 * X[j] * error
        weights -= learning_rate * grad
    return weights
    pass
