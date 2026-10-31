import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	m = 0
	for i in range(len(gradient)):
		m += (gradient[i] ** 2)
	m **= 0.5

	if m == 0:
		zero_vector = [0.0] * len(gradient)
		return {
			'magnitude': 0.0,
            'direction': zero_vector,
            'descent_direction': zero_vector
		}
	
	d = []
	for i in range(len(gradient)):
		d.append(gradient[i] / m)
	dd = []
	for i in range(len(d)):
		dd.append(-d[i])
	return {'magnitude': m, 'direction': [pp for pp in d], 'descent_direction': [x for x in dd]}
	pass