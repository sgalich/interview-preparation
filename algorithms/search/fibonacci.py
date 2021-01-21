from typing import Union, List


def search(arr: List[Union[int, float, str]], S: Union[int, float, str]) -> bool:
	"""Fibonacci search algorithm.
	O(log n)
	"""
	arr = sorted(arr)
	f0 = 0
	f1 = 1
	f2 = f0 + f1
	offset = 0
	# Find min f2 that is > len(arr)
	while f2 <= len(arr):
		f0, f1 = f1, f2
		f2 = f0 + f1
	# Search
	while f1 <= len(arr) and f0 > 0:
		ind = min(offset + f0, len(arr)) - 1
		# print(f'f0: {f0}, f1: {f1}, f2: {f2}, ind: {ind}, arr[ind]: {arr[ind]}')
		if S > arr[ind]:    # cut off the left part
			offset += f0
			f1, f2 = f0, f1
			f0 = f2 - f1 if f2 != 1 else 0    # !!!! IDK how to aboid this check
		elif S < arr[ind]:    # cut off the right part
			f1 -= f0
			f2 = f0
			f0 = f2 - f1 if f2 != 1 else 0    # !!!! IDK how to aboid this check
		else:
			return True
	return False



# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# search(arr, 0)


"""
ERROR! Incorrect answer, input: search([1, 0, 2], 0)
https://www.geeksforgeeks.org/fibonacci-search/
"""
# # Returns index of x if present,  else  
# # returns -1  
# def search(arr, x):
# 	if not arr:    # added by me
# 		return False    # added by me
# 	n = len(arr)    # added by me
# 	# Initialize fibonacci numbers  
# 	fibMMm2 = 0 # (m-2)'th Fibonacci No. 
# 	fibMMm1 = 1 # (m-1)'th Fibonacci No. 
# 	fibM = fibMMm2 + fibMMm1 # m'th Fibonacci 
  
# 	# fibM is going to store the smallest  
# 	# Fibonacci Number greater than or equal to n  
# 	while (fibM < n): 
# 		fibMMm2 = fibMMm1 
# 		fibMMm1 = fibM 
# 		fibM = fibMMm2 + fibMMm1 
  
# 	# Marks the eliminated range from front 
# 	offset = -1; 
  
# 	# while there are elements to be inspected. 
# 	# Note that we compare arr[fibMm2] with x. 
# 	# When fibM becomes 1, fibMm2 becomes 0  
# 	while (fibM > 1): 
		  
# 		# Check if fibMm2 is a valid location 
# 		i = min(offset+fibMMm2, n-1) 
  
# 		# If x is greater than the value at  
# 		# index fibMm2, cut the subarray array  
# 		# from offset to i  
# 		if (arr[i] < x): 
# 			fibM = fibMMm1 
# 			fibMMm1 = fibMMm2 
# 			fibMMm2 = fibM - fibMMm1 
# 			offset = i 
  
# 		# If x is less than the value at  
# 		# index fibMm2, cut the subarray  
# 		# after i+1 
# 		elif (arr[i] > x): 
# 			fibM = fibMMm2 
# 			fibMMm1 = fibMMm1 - fibMMm2 
# 			fibMMm2 = fibM - fibMMm1 
  
# 		# element found. return index  
# 		else : 
# 			return True
  
# 	# comparing the last element with x */ 
# 	if(fibMMm1 and arr[offset+1] == x): 
# 		return True; 
  
# 	# element not found. return -1  
# 	return False



"""
ERROR! Incorrect answer, input: search([1, 0, 2], 0)
https://stackabuse.com/search-algorithms-in-python/#fibonaccisearch
"""
# def search(lys, val):
#     fibM_minus_2 = 0
#     fibM_minus_1 = 1
#     fibM = fibM_minus_1 + fibM_minus_2
#     while (fibM < len(lys)):
#         fibM_minus_2 = fibM_minus_1
#         fibM_minus_1 = fibM
#         fibM = fibM_minus_1 + fibM_minus_2
#     index = -1
#     while (fibM > 1):
#         i = min(index + fibM_minus_2, (len(lys)-1))
#         if (lys[i] < val):
#             fibM = fibM_minus_1
#             fibM_minus_1 = fibM_minus_2
#             fibM_minus_2 = fibM - fibM_minus_1
#             index = i
#         elif (lys[i] > val):
#             fibM = fibM_minus_2
#             fibM_minus_1 = fibM_minus_1 - fibM_minus_2
#             fibM_minus_2 = fibM - fibM_minus_1
#         else :
#             return True
#     if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
#         return True
#     return False
