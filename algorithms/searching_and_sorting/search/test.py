import binary
import jump



IMPLEMENTED_SEARCHES = (
	binary,
	# jump
)

SEARCH_NUM = 0
ARRAYS = (
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
		for array in ARRAYS:
			if (SEARCH_NUM in array) != search_function(array, SEARCH_NUM):
				print(f'ERROR:\narray: {array}')
		print('OK!')


if __name__ == '__main__':
	test()
