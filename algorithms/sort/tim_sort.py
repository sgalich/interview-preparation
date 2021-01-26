from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
	"""TimSort algorithm.
	O(n*log(n))
	"""

	def insertion_sort(array: List[Union[int, float, str]]):
		for i in range(1, len(array)):
			num = array[i]
			if array[i - 1] > num:
				array[i - 1], array[i] = array[i], array[i - 1]
				for j in range(i - 1, 0, -1):
					if array[j - 1] <= array[j]:
						break
					array[j - 1], array[j] = array[j], array[j - 1]

	arr = arr.copy()
	if len(arr) <= 64:
		insertion_sort(arr)
		return arr
	# to be continued...
