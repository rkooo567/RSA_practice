from rsa import Rsa, encoding, decoding

def main():
	""" application """
	bob = Rsa(7, 11)
	bob.select_e()

if __name__ == "__main__":
	main()
