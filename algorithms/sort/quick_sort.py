from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
	"""QuickSort algorithm.
	O(n*log(n)) - O(n^2)
	"""

	# # 1/24/2021
	# # This solution could be done in-place
	# # with a better Space Complexity performance.
	# # But it's not in educational purposes.
	# def partition_around_pivot(start: int, end: int) -> int:
	# 	left = []
	# 	right = []
	# 	pivot = arr[end]
	# 	for i in range(start, end):
	# 		if arr[i] <= pivot:
	# 			left.append(arr[i])
	# 		else:
	# 			right.append(arr[i])
	# 	return left, pivot, right

	# arr = arr.copy()
	# if len(arr) < 2:
	# 	return arr
	# left, pivot, right = partition_around_pivot(0, len(arr) - 1)
	# return sort(left) + [pivot] + sort(right)

	# 2/11/2021
	# In-place solution
	def sort_part(start=0, end=None):
		if not end:
			end = len(arr) - 1
		pivot = arr[end]
		max_left_ind = start
		for i in range(start, end):
			if arr[i] < pivot:
				arr[max_left_ind], arr[i] = arr[i], arr[max_left_ind]
				max_left_ind += 1
		arr[max_left_ind], arr[end] = arr[end], arr[max_left_ind]
		# Sort left part
		new_end = max_left_ind - 1
		if new_end > 0 and new_end > start:
			sort_part(start=start, end=new_end)
		# Sort right part
		new_start = max_left_ind + 1
		if new_start < len(arr) - 1 and new_start < end:
			sort_part(start=new_start, end=end)

	arr = arr.copy()
	if len(arr) < 2:
		return arr
	sort_part()
	return arr


"""
ERROR! maximum recursion depth exceeded in comparison, input: sort([0, 1, 2, 3, 3])
g4g: https://www.geeksforgeeks.org/iterative-quick-sort/
"""
# def sort(arr, low=0, high=None): 

# 	def partition(arr, low, high): 
# 		i = (low - 1)         # index of smaller element 
# 		pivot = arr[high]     # pivot 
# 		for j in range(low, high): 
# 			# If current element is smaller  
# 			# than or equal to pivot 
# 			if arr[j] <= pivot: 
# 				# increment index of 
# 				# smaller element 
# 				i += 1
# 				arr[i], arr[j] = arr[j], arr[i]
# 		arr[i + 1], arr[high] = arr[high], arr[i + 1] 
# 		return (i + 1) 

# 	high = len(arr) - 1 if not high else high
# 	if low < high: 
  
# 		# pi is partitioning index, arr[p] is now 
# 		# at right place 
# 		pi = partition(arr, low, high) 
  
# 		# Separately sort elements before 
# 		# partition and after partition 
# 		sort(arr, low, pi-1) 
# 		sort(arr, pi + 1, high) 
# 	return arr
