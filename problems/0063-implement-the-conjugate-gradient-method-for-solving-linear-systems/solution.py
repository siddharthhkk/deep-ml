import numpy as np
from scipy.sparse.linalg import cg
def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
	"""
	Solve the system Ax = b using the Conjugate Gradient method.

	:param A: Symmetric positive-definite matrix
	:param b: Right-hand side vector
	:param n: Maximum number of iterations
	:param x0: Initial guess for solution (default is zero vector)
	:param tol: Convergence tolerance
	:return: Solution vector x
	"""
	# calculate initial residual vector
	A = np.array(A, dtype=float)
	b = np.array(b, dtype=float)
	x, info = cg(A, b, maxiter=n)
	return x
