import unittest
from typing import Any, Callable

from algorithms.search import linear
from algorithms.search import binary
from algorithms.search import jump
from algorithms.search import interpolation
from algorithms.search import exponential
from algorithms.search import ternary
from algorithms.search import fibonacci
from algorithms.search import dichotomous
from algorithms.search import golden_section
from algorithms.sort import binary_insertion_sort
from algorithms.sort import bubble_sort
from algorithms.sort import bucket_sort
from algorithms.sort import comb_sort
from algorithms.sort import counting_sort
from algorithms.sort import cycle_sort
from algorithms.sort import heap_sort
from algorithms.sort import insertion_sort
from algorithms.sort import merge_sort
from algorithms.sort import pigeonhole_sort
from algorithms.sort import quick_sort
from algorithms.sort import radix_sort
from algorithms.sort import selection_sort
from algorithms.sort import shell_sort
from algorithms.sort import tim_sort
from algorithms.sort import topological_sort


ARRAYS = (
	[],
	[0, 3, 1, 2, 3],
	[0, 5, 1, 2, 3, 4],
	[0, 45, 6, 1, 2, 3, 4, 5],
	[0],
	[1, 0, 2],
	[3, 3, 0],
	[1, 2, 3, 0],
	[1, 0, 2, 3],
	[1, 2, 3, 5, 0],
	[1],
	[-1, 2],
	[-2, -1],
	[-2, -1, -5],
	[-2, -1, 6],
	[2, 1],
	[1, 2],
	[2, 1, 3],
	[1, 2, 3, 4],
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5, 1, 0, 3, 4, 5, 1, 2, 3, 4, 5],
	[0, 2, 3, 467, 5, 1, 23, 3, 4, 54, 12, 2, 3, 4234, 5],
	[0, -2, 3, 467, 5, -1, 23, 3, -4, 54, 12, 2, 3, -4234, 5],
	[-2, 3, 467, 5, -1, 23, 3, -4, 54, 12, 2, 3, -4234, 5, 0]
)


def test_arrays(function_answer: Any, function_test: Callable, *args: Any) -> None:
	print(function_test.__module__, end='\t')
	test_result = 'OK!'
	for array in ARRAYS:
		# print(array)
		_input = f'{function_test.__name__}({array})'
		try:
			answer = function_test(*[array] + list(args))
		except Exception as e:
			test_result = f'ERROR! {e}, input: {_input}'
			break
		if answer != function_answer(array):
			e = 'Incorrect answer'
			test_result = f'ERROR! {e}, input: {_input}, answer: {answer}'
			break
	print(test_result)


##########
# SEARCH #
##########

class TestSearch(unittest.TestCase):
	ALL_SEARCHES = (
		linear,
		binary,
		jump,
		interpolation,
		exponential,
		ternary,
		fibonacci,
		dichotomous,
		golden_section
	)
	SEARCH_NUM = 0

	def test_search(self):
		for search_type in self.ALL_SEARCHES:
			function_test = getattr(search_type, 'search')
			function_answer = lambda x: self.SEARCH_NUM in x
			test_arrays(function_answer, function_test, self.SEARCH_NUM)
					

##########
#  SORT  #
##########

class TestSort(unittest.TestCase):
	ALL_SORTS = (
		binary_insertion_sort,
		bubble_sort,
		bucket_sort,
		comb_sort,
		counting_sort,
		cycle_sort,
		heap_sort,
		insertion_sort,
		merge_sort,
		pigeonhole_sort,
		quick_sort,
		radix_sort,
		selection_sort,
		shell_sort,
		tim_sort,
		topological_sort
	)

	def test_sort(self):
		for search_type in self.ALL_SORTS:
			function_test = getattr(search_type, 'sort')
			function_answer = lambda x: sorted(x)
			test_arrays(function_answer, function_test)


if __name__ == '__main__':
	# functions = (
	# 	test_search,
	# 	test_sort
	# )
	# for function in functions:
	# 	function()
	unittest.main()
