#!/usr/bin/python3
def magic_calculation(a, b):
	"""Bytecode decompilation"""
	from magic_calculation_102 import add, sub

	if a < b:
		c = add(a, b)

		for i in range(4, 6):
			c = add(a, b)
		return (c)
	else:
		return(sub(a, b))
	
