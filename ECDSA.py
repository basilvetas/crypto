# Basil Vetas
# 4/20/16

import EC
import hashlib
import random

# https://docs.python.org/2/library/hashlib.html#module-hashlib
# m = hashlib.sha256()
# m.update("Honesty is the fist chapter in thge book of wisdom. Thomas Jefferson")
# s = m.digest()
# s
# len(s)
# s = m.hexdigest()
# s
# int(s, 16)


# Hash function for a message m mod n
def HashMessage(message, n):
	h = hashlib.sha256()
	h.update(message)
	s = h.hexdigest()
	val = int(s, 16)
	return # DO STUFF

# Elliptic Curve Digital Signature Algorithm (ECDSA)
# Note every signature you create with this algorithm will be different, 
# even for the same message m. This is because of the randonly chosen k
def sign(m, Q, n, Elist, char):
	# m is the message
	# d is the private key
	# Q is my point
	# n = ord(Q) is the prime number I already computed elsewhere
	# (or someone computed for me)
	# Elist is my elliptic curve
	# char is the characteristic
	z = HashMessage(m, n)
	myRand = random.SystemRandom() # a cryptographically secure random number generator
	r = 0
	while(r == 0):
		k = myRand.randint(1, n-1)
		kQ = EC.nP(k, Q, Elist, char)

		# DO STUFF
		r = x1%n
	# DO STUFF
	return [r, s]






