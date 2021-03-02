def convert_decimal(n: int, base: int) -> str:
	"""Converts decimal number to base system,
	where base <= 10.
	"""
	# # Recursive solution
	# if n < 0:
	# 	return '-' + convert_decimal(-n, base)
	# if n < base:
	# 	return str(n)
	# return convert_decimal(n // base, base) + str(n % base)

	# Iterative solution
	new_num = ''
	abs_num = abs(n)
	while abs_num >= base:
		new_num += str(abs_num % base)
		abs_num //= base
	new_num += str(abs_num)
	new_num  = new_num[::-1] if n >= 0 else '-' + new_num[::-1]
	return new_num
