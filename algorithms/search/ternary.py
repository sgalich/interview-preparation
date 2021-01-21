from typing import Union, List


def search(arr: List[Union[int, float, str]], S: Union[int, float, str]) -> bool:
	"""Ternary search algorithm.
	O(log3 n)
	"""
	arr = sorted(arr)
	start = 0
	end = len(arr) - 1
	while start <= end:
		step = (end - start) // 3
		ind_1 = start + step
		ind_2 = ind_1 + step
		if arr[ind_1] == S or arr[ind_2] == S:
			return True
		elif S < arr[ind_1]:
			end = ind_1 - 1
		elif S > arr[ind_2]:
			start = ind_2 + 1
		else:
			start += 1
			end -= 1
	return False


"""
g4g
did NOT PASS: maximum recursion depth exceeded while calling a Python object
https://www.geeksforgeeks.org/binary-search-preferred-ternary-search/
"""
# def search(arr, x, l=0, r=None):
# 	if not arr:
# 		return False
# 	r = len(arr) if not r else r
# 	if (r >= l): 
# 		mid1 = l + (r - l)//3
# 		mid2 = mid1 + (r - l)//3
   
# 		# If x is present at the mid1 
# 		if arr[mid1] == x: 
# 			return True 
   
# 		# If x is present at the mid2 
# 		if arr[mid2] == x: 
# 			return True 
   
# 		# If x is present in left one-third 
# 		if arr[mid1] > x: 
# 			return search(arr, x, l, mid1-1) 
   
# 		# If x is present in right one-third 
# 		if arr[mid2] < x: 
# 			return search(arr, x, mid2+1, r) 
   
# 		# If x is present in middle one-third 
# 		return search(arr, x, mid1+1, mid2-1) 
	 
# 	# We reach here when element is not present in array 
# 	return False
