from rsa import Rsa, encoding, decoding

def main():
	""" application """
	print("Hi, this is the program that shows you RSA encryption.\n")
	user_name = input("What's your name? : ")
	p = int(input("\nChoose your p : "))
	q = int(input("Choose your q : "))
	user = Rsa(user_name, p, q)
	user.select_e()
	print(
		"\n User name : ", user.user_name,
		"\n p and q : ", user.p, user.q,
		"\n public key :", user.get_public_key(),
		"\n private key :", user.get_private_key()
		)

if __name__ == "__main__":
	main()
