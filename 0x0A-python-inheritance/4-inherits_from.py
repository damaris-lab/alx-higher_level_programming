#!/usr/bin/python3

"""inherits fro function definition
"""


def inherits_from(obj, a_class):
	
	"""
	function returns True:object is class instance that
	inherited from pecified class(directly or indirectly)
	else:False
	"""
	
	return issubclass(type(obj), a_class) and type(obj) != a_class
