import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # Your code here
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)
    weights = np.array(weights, dtype=float)
    m, n = X.shape
    for i in range(n_epochs):
        if method == 'batch':
            prediction = X @ weights
            error = prediction - y
            gradient = (2 / m) * (X.T @ error)
            weights -= learning_rate * gradient

        elif method == 'stochastic':
            for j in range(m):
                xi = X[j]
                yi = y[j]
                prediction = np.dot(xi, weights)
                error = prediction - yi
                gradient = 2 * xi * error  
                weights -= learning_rate * gradient

        elif method == 'mini_batch':
            for j in range(0, m, batch_size):
                X_batch = X[j:j + batch_size]
                y_batch = y[j:j + batch_size]
                m_b = len(X_batch)
                
                prediction = X_batch @ weights
                error = prediction - y_batch
                gradient = (2 / m_b) * (X_batch.T @ error)
                weights -= learning_rate * gradient
    
    return weights
    
    pass
