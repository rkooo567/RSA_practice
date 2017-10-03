# util function

def is_prime(n):
	""" calculate prime number
	>>> is_prime(4)
	False
	>>> is_prime(7)
	True
	>>> is_prime(17)
	True
	>>> is_prime(23)
	True
	>>> is_prime(60)
	False
	>>> is_prime(93)
	True
	"""
	if n % 2 == 0:
		return False
	else:
		for i in range(3, n // 2 + 1):
			if n // i == 0:
				return False
		return True

def char_to_binary(chr):
	""" change char to binary"""
	return int(bin(ord(chr)), 2)

def binary_to_char(binary_char):
	""" convert binary list to the string"""
	return bin(binary_char)
