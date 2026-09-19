import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape != v2.shape:
		raise ValueError("Inputs require the same shape")

	norm_v1 = float(np.sqrt(np.dot(v1, v1).sum()))
	norm_v2 = float(np.sqrt(np.dot(v2, v2).sum()))
	
	if norm_v1 == 0 or norm_v2 == 0:
		raise ValueError("Inputs can't be zero vector")
	
	return np.dot(v1, v2) / (norm_v1 * norm_v2)
	