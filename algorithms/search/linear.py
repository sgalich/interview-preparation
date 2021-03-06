from typing import Union, List


def search(arr: List[Union[int, float, str]], S: Union[int, float, str]) -> bool:
	"""Linear search algorithm.
	O(n)
	"""
	for i in range(len(arr)):
		if arr[i] == S:
			return True
	return False
