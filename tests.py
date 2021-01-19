from algorithms.search import linear
from algorithms.search import binary
from algorithms.search import jump
from algorithms.search import interpolation
from algorithms.search import exponential
from algorithms.search import ternary
from algorithms.search import fibonacci


##########
# SEARCH #
##########

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
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5, 1, 0, 3, 4, 5, 1, 2, 3, 4, 5],
	[0, 2, 3, 467, 5, 1, 23, 3, 4, 54, 12, 2, 3, 4234, 5],
	[0, -2, 3, 467, 5, -1, 23, 3, -4, 54, 12, 2, 3, -4234, 5]
)


def test_search():
	for search_type in IMPLEMENTED_SEARCHES:
		search_function = getattr(search_type, 'search')
		print(search_function.__module__, end='\t')
		test_result = 'OK!'
		for array in ARRAYS:
			_input = f'{search_function.__name__}({array}, {SEARCH_NUM})'
			try:
				answer = search_function(array, SEARCH_NUM)
			except Exception as e:
				test_result = f'ERROR! {e}, input: {_input}'
				break
			if (SEARCH_NUM in array) != answer:
				e = 'Incorrect answer'
				test_result = f'ERROR! {e}, input: {_input}'
				break
		print(test_result)


##########
#  SORT  #
##########

def test_sort():
	pass


if __name__ == '__main__':
	functions = (
		test_search,
		test_sort
	)
	for function in functions:
		function()
