from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
	"""Ghnome sort algorithm.
	O(n^2)
	"""
	arr = arr.copy()
	i = 1
	while i < len(arr):
		if i == 0 or arr[i - 1] <= arr[i]:
			i += 1
		else:
			arr[i - 1], arr[i] = arr[i], arr[i - 1]
			i -= 1
	return arr
