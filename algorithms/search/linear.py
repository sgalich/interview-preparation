def search(arr, S):
	"""Linear search algorithm.
	O(n)
	"""
	for i in range(len(arr)):
		if arr[i] == S:
			return True
	return False
