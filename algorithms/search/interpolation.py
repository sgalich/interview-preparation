from typing import Union, List


def search(arr: List[Union[int, float, str]], S: Union[int, float, str]) -> bool:
	"""Interpolation search algorithm.
	O(log log n) - O(n)
	"""

	def estimate_index():
		estimated_gap = (arr[high] - arr[low]) / (high - low)
		estimated_gap = 1 if not estimated_gap else estimated_gap
		index = low + int((S - arr[low]) / estimated_gap)
		index = 0 if index < 0 else index
		return min(index, high)    # for this case: # [-2, -1]

	arr = sorted(arr)    # this search works only with sorted arrays
	low = 0
	high = len(arr) - 1
	while low <= high:
		# Edge case + base case breaking the while loop
		if low == high:
			return arr[low] == S
		index = estimate_index()
		num = arr[index]
		if S == num:
			return True
		elif S < num:
			high -= 1
		else:
			low += 1
	return False


"""
G4g - do not goes through my tests :)
https://www.geeksforgeeks.org/interpolation-search/
niether as this example:
"""
# def search(arr, x, lo=0, hi=None):
# 	print(arr)
# 	hi = len(arr) - 1 if not hi else hi
# 	# Since array is sorted, an element present
# 	# in array must be in range defined by corner
# 	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
# 		# Probing the position with keeping
# 		# uniform distribution in mind.
# 		pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
# 					(x - arr[lo]))
 
# 		# Condition of target found
# 		if arr[pos] == x:
# 			return True
 
# 		# If x is larger, x is in right subarray
# 		if arr[pos] < x:
# 			return interpolationSearch(arr, x, pos + 1,
# 									   hi)
 
# 		# If x is smaller, x is in left subarray
# 		if arr[pos] > x:
# 			return interpolationSearch(arr, x, lo,
# 									   pos - 1)
# 	return False


"""
...niether as this example:
https://stackabuse.com/search-algorithms-in-python/#interpolationsearch
"""
# def search(lys, val):
#     low = 0
#     high = (len(lys) - 1)
#     while low <= high and val >= lys[low] and val <= lys[high]:
#         index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
#         if lys[index] == val:
#             return True
#         if lys[index] < val:
#             low = index + 1;
#         else:
#             high = index - 1;
#     return False
