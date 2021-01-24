from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
	"""Bubble sort algorithm.
	O( ? )
	"""
	arr = arr.copy()
	if len(arr) < 2:
		return arr
	swap = True
	ordered = 0    # offset from the right part (not to iterate already sorted part)
	while swap:
		swap = False
		for i in range(len(arr) - ordered - 1):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swap = True
		ordered += 1
	return arr
