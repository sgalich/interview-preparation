from algorithms.search import linear
from algorithms.search import binary
from algorithms.search import jump
from algorithms.search import interpolation
from algorithms.search import exponential
from algorithms.search import ternary
from algorithms.search import fibonacci


IMPLEMENTED_SEARCHES = (
	linear,
	binary,
	jump,
	interpolation,
	exponential,
	ternary,
	fibonacci
)
SEARCH_NUM = 0
ARRAYS = (
	[],
	[0, 1, 2, 3],
	[0],
	[1, 0, 2],
	[3, 3, 0],
	[1, 2, 3, 0],
	[1, 0, 2, 3],
	[1],
	[2, 1, 3],
	[1, 2, 3, 4],
	[1, 2, 3, 4, 5]
)


def test():
	for search_type in IMPLEMENTED_SEARCHES:
		search_function = getattr(search_type, 'search')
		print(search_function.__module__, end='\t')
		is_error = 'OK!'
		for array in ARRAYS:
			if (SEARCH_NUM in array) != search_function(array, SEARCH_NUM):
				is_error = f'ERROR! array: {array}'
				break
		print(is_error)


if __name__ == '__main__':
	test()
