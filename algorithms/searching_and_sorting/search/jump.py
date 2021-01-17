def search(arr, S):
	"""Jump search algorithm.
	O(√n) for sorted array
	"""
	arr.sort()    # Jump search is for sorted arrays only
	step = int(len(arr)**.5)
	end = step
	while end <= len(arr):
		if arr[end - 1] >= S:
			# If number S should be in this interval =>
			# do a linear search
			for i in range(end - step, end):
				if arr[i] == S:
					return True
		else:    # Jump to another interval
			end += step
	return False
