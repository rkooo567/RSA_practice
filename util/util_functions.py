# util function

from fractions import gcd

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

def egcd(x, y):
	""" 
	return (d, a, b) a*x + b*y = gcd(x, y) := d 
	
	>>> egcd(16, 10)
	(2, 2, -3)

	"""
	if y == 0:
		return (x, 1, 0)
	else:
		d, a, b = egcd(y, x % y)
		return d, b, (a - (x // y) * b)

def multiplicative_inverse(a, m):
	""" 
	find multiplicative inverse of a mod m
	
	>>> multiplicative_inverse(2, 5)
	3
	>>> multiplicative_inverse(1, 6)
	1
	>>> multiplicative_inverse(-1, 6)
	5
	>>> multiplicative_inverse(9, 10)
	9
	"""
	return egcd(a, m)[1] % m