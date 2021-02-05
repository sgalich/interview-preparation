from typing import Union, List
import math


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
	"""Bucket sort algorithm.
	O( ? )
	"""

	def estimate_index(num: Union[int, float]) -> int:
		"""Estimates a bucket index for the num."""
		# return int(len(arr) * num / max_num)    # why?! source: wikipedia
		step = (max_num - min_num) / (len(arr) - 1)
		step = math.ceil(step)
		ind = (num - min_num) // step if step else 0
		return ind
	
	def insertion_sort(array: Union[str, float, int]) -> None:
		# print(array, range(1, len(array)))
		# [1, 5, 9, 3] i=3, j=2 => replace
		# [1, 5, 3, 9] i=3, j=1 => replace
		# [1, 3, 5, 9] i=3, j=0 => break
		for i in range(1, len(array)):
			for j in range(i - 1, -1, -1):
				if array[j] > array[j + 1]:
					array[j], array[j + 1] = array[j + 1], array[j]
				else:
					break
		return array

	def binary_insertion_sort(arr: Union[str, float, int]) -> None:

		def binary_search() -> int:
			start = 0
			end = i + 1
			while start < end:
				ind = start + (end - start) // 2
				# Case to go to the left
				if ind > 0 and arr[ind - 1] > num:
					end = ind
				# Case to go to the right
				elif arr[ind] < num:
					start = ind + 1
				else:
					return ind

		for i in range(1, len(arr)):
			num = arr[i]
			ind = binary_search()
			arr = arr[:ind] + [num] + arr[ind:i] + arr[i + 1:]
		return arr

	if len(arr) < 2:
		return arr
	arr = arr.copy()
	buckets = [[] for _ in range(len(arr))]
	min_num, max_num = min(arr), max(arr)
	if min_num == max_num:
		return arr
	# 1. Distribute numbers by buckets
	for i in range(len(arr)):
		num = arr[i]
		ind = estimate_index(num)
		buckets[ind].append(num)
	# 2. Sort buckets
	# buckets = [sort(bucket) for bucket in buckets]    # recursive sort
	# buckets = [insertion_sort(bucket) for bucket in buckets]    # insertion sort with linear search
	buckets = [binary_insertion_sort(bucket) for bucket in buckets]    # insertion sort with binary search
	# 3. Concatenate sorted buckets
	output = []
	for bucket in buckets:
		output += bucket
	return output


"""
ERROR! list index out of range, input: sort([1, 0])
g4g: https://www.geeksforgeeks.org/bucket-sort-2/
"""
# def insertionSort(b): 
# 	for i in range(1, len(b)): 
# 		up = b[i] 
# 		j = i - 1
# 		while j >= 0 and b[j] > up:  
# 			b[j + 1] = b[j] 
# 			j -= 1
# 		b[j + 1] = up      
# 	return b      
			  
# def sort(x): 
# 	if len(x) < 2:
# 		return x
# 	arr = [] 
# 	slot_num = 10 # 10 means 10 slots, each 
# 				  # slot's size is 0.1 
# 	for i in range(slot_num): 
# 		arr.append([]) 
		  
# 	# Put array elements in different buckets  
# 	for j in x: 
# 		index_b = int(slot_num * j)  
# 		arr[index_b].append(j) 
	  
# 	# Sort individual buckets  
# 	for i in range(slot_num): 
# 		arr[i] = insertionSort(arr[i]) 
		  
# 	# concatenate the result 
# 	k = 0
# 	for i in range(slot_num): 
# 		for j in range(len(arr[i])): 
# 			x[k] = arr[i][j] 
# 			k += 1
# 	return x 
