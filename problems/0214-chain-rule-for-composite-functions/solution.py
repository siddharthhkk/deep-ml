import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	theta = 1
	curr = x
	for i in range(len(functions) -1, -1, -1):
		if functions[i] == 'sin': 
			theta *= np.cos(curr)
			curr = np.sin(curr)
		elif functions[i] == 'square':
			theta *= 2 * curr
			curr = curr ** 2
		elif functions[i] == 'exp': 
			theta *= np.exp(curr)
			curr = np.exp(curr)
		elif functions[i] == 'log': 
			theta *= 1.0 / curr
			curr = np.log(curr)
	return float(theta)
	pass