from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
	"""Heap sort algorithm.
	O( ? )
	"""
	# # ERROR! Incorrect answer, input: sort([0, 3, 1, 2, 3], answer: [2, 3, 3, 1, 0]
	# def heapify(arr, n, i):    # [2, 5, 4, 7, 10], 3, 0
	# 	largest = i  # Initialize largest as root    # 0
	# 	l = 2 * i + 1     # left = 2*i + 1    # 1
	# 	r = 2 * i + 2     # right = 2*i + 2    # 2
	# 	# See if left child of root exists and is
	# 	# greater than root
	# 	if l < n and arr[largest] < arr[l]:    # 4<5?
	# 		largest = l    # 1
	# 	# See if right child of root exists and is
	# 	# greater than root
	# 	if r < n and arr[largest] < arr[r]:    # 7?
	# 		largest = r    # 2
	# 	# Change root, if needed
	# 	if largest != i:    # 2!=0
	# 		arr[i], arr[largest] = arr[largest], arr[i]  # swap: [7, 5, 4, 2, 10]
	# 		# Heapify the root.
	# 		heapify(arr, len(arr), largest)
 
	# arr = arr.copy()    # [4, 5, 7, 2, 10]
	# # Build a maxheap.
	# for i in range(len(arr) // 2 - 1, -1, -1):    # 1-0
	# 	heapify(arr, len(arr), i)
	# # One by one extract elements    # [10, 5, 7, 2, 4]
	# for i in range(len(arr) - 1, 0, -1):    # 4-1: 3
	# 	arr[i], arr[0] = arr[0], arr[i]  # swap: [2, 5, 4, 7, 10]
	# 	heapify(arr, i, 0)
	# return arr
	pass
	# may be somewhen...

		



"""
def heapify(arr, n, i):
	largest = i  # Initialize largest as root
	l = 2 * i + 1     # left = 2*i + 1
	r = 2 * i + 2     # right = 2*i + 2
 
	# See if left child of root exists and is
	# greater than root
	if l < n and arr[largest] < arr[l]:
		largest = l
 
	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r
 
	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
		# Heapify the root.
		heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
	n = len(arr)
 
	# Build a maxheap.
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)
 
	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]  # swap
		heapify(arr, i, 0)
"""
