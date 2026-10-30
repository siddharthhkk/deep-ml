import numpy as np
def lu_decomposition(A: list) -> tuple:
	"""
	Perform LU decomposition on a square matrix using Doolittle's method.
	
	Args:
		A: Square matrix as a list of lists
	
	Returns:
		tuple: (L, U) where L is lower triangular with 1s on diagonal,
		       U is upper triangular, and A = L @ U
	"""
	U = np.array(A, dtype=float)
	n = U.shape[0]
	L = np.eye(n)
	for i in range(n - 1):
		factors = U[i+1:, i] / U[i, i]
		L[i+1:, i] = factors
		U[i+1:, i:] -= factors[:, np.newaxis] * U[i, i:]
	
	return L, U