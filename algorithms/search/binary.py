from typing import Union, List


def search(arr: List[Union[int, float, str]], S: Union[int, float, str]) -> bool:
	"""Binary search algorithm.
	O(log(n)) for sorted array
	"""
	arr = sorted(arr)
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
