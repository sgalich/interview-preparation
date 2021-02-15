from typing import Union, List


def sort(arr: List[Union[int]]) -> List[Union[int]]:
	"""Radix sort algorithm.
	O( ? )
	"""

	def counting_sort(i: int) -> List[Union[int]]:

		def get_digit(number: int) -> int:
			try:
				n = str(number)[-i - 1]
			except IndexError:
				return 0
			return int(n)
	
		# 1. Set a range
		count = [0] * 10
		# 2. Count the quantity of each number
		for num in arr:
			n = get_digit(num)
			count[n] += 1
		# 3. Count accumulative quantity
		for j in range(1, len(count)):
			count[j] += count[j - 1]
		# 4. Generate output array
		output = [0] * len(arr)
		# Here we moving backwards in order to save
		# the order of nums we meet - this is essential
		for j in range(len(arr) - 1, -1, -1):
			num = arr[j]
			n = get_digit(num)
			count[n] -= 1
			ind = count[n]
			output[ind] = num
		return output			
	
	if len(arr) < 2 or min(arr) < 0:
		return sorted(arr)
	arr = arr.copy()
	repetitions = len(str(max(arr)))
	for i in range(repetitions):
		arr = counting_sort(i)
	return arr
