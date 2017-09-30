# file to implement RSA

from fractions import gcd

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

def binary_to_chr(binary_char):
	""" convert binary list to the string"""
	return bin(binary_char)

# functions for decoding and encoding
def encoding(public_key, message):
	n = public_key[0]
	e = public_key[1]
	return message ** e % n

def decoding(private_key, decoded_message):
	n = private_key[0]
	d = private_key[1]
	return decoded_message ** d % n

class Rsa(object):
	"""
	Implement RSA cryptography algorithm for pratices.
	"""
	def __init__(self, p, q, e=None):
		"""
		determine the value N in x^e (mod N)
		p ,q : prime numbers
		e : relatively prime to (p-1)*(q-1)
		"""
		assert e == None or gcd((p-1)*(q-1), e) == 1, "e has to be coprime to (p-1)(q-1)"
		self.p = p # prime p
		self.q = q # prime q
		self.n = self.p * self.q # N
		self.p_1_q_1 = (self.p - 1) * (self.q - 1) # (p-1) * (q-1)
		self.e = e # e is None initially. 
		self.d = self.calculate_d(self.e) # calculate d, multiplicative inverse of e mod ((p-1)(q-1))
		self.public_key = (self.n, self.e)
		self.private_key = (self.n, self.d)

	def select_e(self):
		"""
		show selection of e and decide the e value after that using e, calculate d,
			multiplicative inverse of e mod((p-1)(q-1))
		""" 
		e_list = []
		for i in range(2, self.p_1_q_1):
			if gcd(self.p_1_q_1, i) == 1:
				e_list.append(i)
		print("list of e : ", e_list)
		self.e = int(input("choose one e : "))
		self.update_keys()

	def update_keys(self):
		""" based on e and d, change the public and private key"""
		self.d = self.calculate_d(self.e)
		self.public_key = (self.n, self.e)
		self.private_key = (self.n, self.d)

	def calculate_d(self, e):
		""" 
		calculate d, multiplicative inverse of e, when e is not None
		"""
		if e == None:
			return None
		else:
			d = 2
			while True:
				if (e * d) % self.p_1_q_1 == 1:
					return d # if d satisfies ed = 1 mod ((p-1)(q-1)), d is the return value
				else:
					d += 1

	def get_public_key(self):
		""" return the tuple, public key"""
		return self.public_key

	def get_private_key(self):
		return self.private_key



		