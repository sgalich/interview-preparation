def search(arr, S):
	"""Binary search algorithm.
	O(log(n)) for sorted array
	"""
	arr.sort()
	start = 0
	end = len(arr)
	while start < end:
		ind = start + int((end - start) / 2)
		num = arr[ind]
		# print(start, end, ind, num)
		if num == S:
			return True
		elif num < S:
			start = ind + 1
		else:
			end = ind
	return False
