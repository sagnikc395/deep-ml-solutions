import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	arr = np.array(matrix)

	if mode == "row":
		return np.mean(arr,axis=1)
	else:
		return np.mean(arr,axis=0)
