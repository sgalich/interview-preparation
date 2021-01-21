from typing import Union, List


def search(arr: List[Union[int, float, str]], S: Union[int, float, str]) -> bool:
	"""Exponential search algorithm.
	O(1) - O(log n)
	"""

	def binarySearch(start: int, end: int) -> bool:
		while start <= end:
			ind = start + int((end - start) / 2)
			if arr[ind] < S:
				start = ind + 1
			elif arr[ind] > S:
				end = ind - 1
			else:
				return True
		return False

	if not arr:
		return False
	if arr[0] == S:
		return True
	arr = sorted(arr)
	i = 1
	while i < len(arr) and arr[i] <= S:
		i *= 2
	return binarySearch(int(i / 2), min(i, len(arr)))


"""
G4g code - did NOT pass
https://www.geeksforgeeks.org/exponential-search/
"""
# present, otherwise -1
# def binarySearch( arr, l, r, x):
# 	if r >= l:
# 		mid = l + ( r-l ) / 2
		 
# 		# If the element is present at 
# 		# the middle itself
# 		if arr[mid] == x:    # TypeError: list indices must be integers or slices, not float
# 			return True
		 
# 		# If the element is smaller than mid, 
# 		# then it can only be present in the 
# 		# left subarray
# 		if arr[mid] > x:
# 			return binarySearch(arr, l, 
# 								mid - 1, x)
		 
# 		# Else he element can only be
# 		# present in the right
# 		return binarySearch(arr, mid + 1, r, x)
		 
# 	# We reach here if the element is not present
# 	return False
 
# # Returns the position of first
# # occurrence of x in array
# def search(arr, x):
# 	n = len(arr)
# 	# IF x is present at first 
# 	# location itself
# 	if arr[0] == x:    # IndexError: list index out of range
# 		return True
		 
# 	# Find range for binary search 
# 	# j by repeated doubling
# 	i = 1
# 	while i < n and arr[i] <= x:
# 		i = i * 2
	 
# 	# Call binary search for the found range
# 	return binarySearch( arr, i / 2, 
# 						 min(i, n-1), x)
# 			# Error here: i/ 2 is float & we use it as an index!


"""
passed with corrections (see "my addition)
https://stackabuse.com/search-algorithms-in-python/#exponentialsearch
"""
# def search(lys, val):

# 	def BinarySearch(lys, val):
# 		first = 0
# 		last = len(lys)-1
# 		index = -1
# 		while (first <= last) and (index == -1):
# 			mid = (first+last)//2
# 			if lys[mid] == val:
# 				index = mid
# 			else:
# 				if val<lys[mid]:
# 					last = mid -1
# 				else:
# 					first = mid +1
# 		ans = False if index == -1 else True
# 		return ans

# 	if not lys:    # my addition
# 		return False    # my addition
# 	if lys[0] == val:
# 		return True
# 	index = 1
# 	while index < len(lys) and lys[index] <= val:
# 		index = index * 2
# 	# return BinarySearch( arr[:min(index, len(lys))], val)    # arr???
# 	return BinarySearch( lys[:min(index, len(lys))], val)    # my addition
