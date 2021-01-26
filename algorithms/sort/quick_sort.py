from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
	"""QuickSort algorithm.
	O(n*log(n)) - O(n^2)
	This solution could be done in-place
	with a better Space Complexity performance.
	But it's not in educational purposes.
	"""

	def partition_around_pivot(start: int, end: int) -> int:
		left = []
		right = []
		pivot = arr[end]
		for i in range(start, end):
			if arr[i] <= pivot:
				left.append(arr[i])
			else:
				right.append(arr[i])
		return left, pivot, right

	arr = arr.copy()
	if len(arr) < 2:
		return arr
	left, pivot, right = partition_around_pivot(0, len(arr) - 1)
	return sort(left) + [pivot] + sort(right)



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
