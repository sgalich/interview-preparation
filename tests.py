import unittest
from typing import Any, Callable
import random
import time

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
	[], [0], [1],
	[0, 3, 1, 2, 3],
	[0, 5, 1, 2, 3, 4],
	[0, 45, 6, 1, 2, 3, 4, 5],
	[1, 0, 2],
	[3, 3, 0],
	[1, 2, 3, 0],
	[1, 0, 2, 3],
	[1, 2, 3, 5, 0],
	[0] + random.sample(range(-1000000, 1000000), 1),
	[0] + random.sample(range(-1000000, 1000000), 2),
	[0] + random.sample(range(-1000000, 1000000), 3),
	[0] + random.sample(range(-1000000, 1000000), 4),
	[0] + random.sample(range(-1000000, 1000000), 5),
	random.sample(range(-1000000, 1000000), 1),
	random.sample(range(-1000000, 1000000), 2),
	random.sample(range(-1000000, 1000000), 3),
	random.sample(range(-1000000, 1000000), 4),
	random.sample(range(-1000000, 1000000), 5),
	[0] + random.sample(range(-1000000, 1000000), 10),
	[0] + random.sample(range(-1000000, 1000000), 100),
	[0] + random.sample(range(-1000000, 1000000), 1000),
	[0] + random.sample(range(-1000000, 1000000), 10000),
	# [0] + random.sample(range(-1000000, 1000000), 100000),
	# [0] + random.sample(range(-1000000, 1000000), 1000000),
	random.sample(range(-1000000, 1000000), 10),
	random.sample(range(-1000000, 1000000), 100),
	random.sample(range(-1000000, 1000000), 1000),
	random.sample(range(-1000000, 1000000), 10000),
	# random.sample(range(-1000000, 1000000), 100000),
	# random.sample(range(-1000000, 1000000), 1000000),
)


def test_arrays(function_answer: Callable, function_test: Callable, *args: Any) -> None:
	print(function_test.__module__, end='\t\t')
	test_result = 'OK!'
	start = time.time()
	running_time = ''
	for array in ARRAYS:
		# print(array)
		_input = f'{function_test.__name__}({array})'
		try:
			answer = function_test(*[array] + list(args))
		except Exception as e:
			test_result = f'ERROR! {e}, input: {_input}'
			break
		# print(answer)
		if answer == None:
			test_result = 'Is not implemented yet.'
			break
		if answer != function_answer(array):
			e = 'Incorrect answer'
			test_result = f'ERROR! {e}, input: {_input[:20]}, answer: {answer[:20]}'
			break
		running_time = time.time() - start
		running_time = '{:.2f}'.format(running_time)
	print(test_result, running_time)


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
