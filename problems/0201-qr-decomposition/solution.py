import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
	"""
	Perform QR decomposition using Gram-Schmidt process.
	
	Args:
		A: An m x n matrix represented as list of lists
	
	Returns:
		Tuple of (Q, R) where Q is orthogonal and R is upper triangular
	"""
	# Your code here
	Q, R = np.linalg.qr(np.array(A, dtype=float))
	ph = np.sign(np.diag(R))
	ph[ph==0] = 1
	Q = Q*ph
	R = R*ph[:,np.newaxis]
	return Q.tolist(), R.tolist()
	pass