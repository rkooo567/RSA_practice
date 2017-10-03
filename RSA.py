# file to implement RSA

from fractions import gcd
from util.util_functions import is_prime, char_to_binary, binary_to_char, egcd, multiplicative_inverse

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
	def __init__(self, user_name, p, q, e=None):
		"""
		determine the value N in x^e (mod N)
		p ,q : prime numbers
		e : relatively prime to (p-1)*(q-1)
		"""
		assert is_prime(p) and is_prime(q), "p and q have to be prime numbers"
		assert e == None or gcd((p-1)*(q-1), e) == 1, "e has to be coprime to (p-1)(q-1)"
		self.user_name = user_name
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
			return multiplicative_inverse(self.e, self.p_1_q_1)

	def get_public_key(self):
		""" return the tuple, public key"""
		assert self.e != None, "e has not been chosen" 
		return self.public_key

	def get_private_key(self):
		assert self.e != None, "e has not been chosen" 
		return self.private_key



		