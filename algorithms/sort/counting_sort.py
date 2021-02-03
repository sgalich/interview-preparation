from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
	"""Counting sort algorithm.
	O(n + k)
	This algorithm is supposed to sort only positive integers.
	"""
	if len(arr) < 2:
		return arr
	if min(arr) < 0:
		return sorted(arr)
	count = [0] * (max(arr) + 1)
	# 1. Count how many each of the numbers do we have
	for num in arr:
		count[num] += 1
	# 2. Count accumulative sums
	for i in range(1, len(count)):
		count[i] += count[i - 1]
	# 3. Set each of the numbers on treir places
	output = [0] * len(arr)
	for num in arr:
		count[num] -= 1
		ind = count[num]
		output[ind] = num
	return output
