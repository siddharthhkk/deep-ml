import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    num_grad = np.zeros_like(x, dtype=float)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        val = x[idx]
        x[idx] = val + epsilon
        fx_plus = f(x)
        x[idx] = val - epsilon
        fx_minus = f(x)
        x[idx] = val
        num_grad[idx] = (fx_plus - fx_minus) / (2 * epsilon)
        it.iternext()
    num = np.linalg.norm(num_grad - analytical_grad)
    den = np.linalg.norm(num_grad) + np.linalg.norm(analytical_grad)
    rel_error = num / den if den > 0 else 0.0
    return num_grad, rel_error
    pass