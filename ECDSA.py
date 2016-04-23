# Basil Vetas
# 4/20/16

import EC
import hashlib
import random

# Elliptic Curve Digitial Signature Algorithm implementation

# Python reference for hash algorithms:
# https://docs.python.org/2/library/hashlib.html#module-hashlib

# example use:
# m = hashlib.sha256()
# m.update("Honesty is the fist chapter in thge book of wisdom. Thomas Jefferson")
# s = m.digest()
# s
# len(s)
# s = m.hexdigest()
# s
# int(s, 16)

# Hash function for a message m mod n
# params:
# 	m is the message
# 	n is the characteristic
def HashMessage(message, n):
	h = hashlib.sha256() # load a hash object
	h.update(message) # hash the message into the object
	s = h.hexdigest() # turns the hashed msg into a hexidecimal

	e = int(s, 16) # turns the hexidecimal into an integer
	pow(2, e + 1000, n) # returns a number between 0 and n-1
	return e%n

# Elliptic Curve Digital Signature Algorithm (ECDSA)
# Note every signature you create with this algorithm will be different, 
# even for the same message m. This is because of the randonly chosen k
# params:
# 	m is the message
# 	d is the private key
# 	Q is my point
# 	n = ord(Q) is the prime number I already computed elsewhere
# 	Elist is my elliptic curve
# 	char is the characteristic
def sign(m, d, Q, n, Elist, char):
	z = HashMessage(m, n)
	myRand = random.SystemRandom() # a cryptographically secure random number generator
	r = 0
	while(r == 0):
		k = myRand.randint(1, n-1)
		kQ = EC.nP(k, Q, Elist, char)
		r = kQ[0]%n # if r = 0 we will keep looping
		
		# only compute s if r is not zero
		if(r != 0):
			k_inv = EC.invMod(k, n)	
			s = (k_inv*(z + r*d))%n
			if(s == 0): # if s equals 0
				r = 0	# choose a new k and compute r and s again
		
	return [r, s]

# ECDSA validation algorithm
# get signature by:
# 	signature = EC.sign(m, d, Q, n, Elist, char)
def validate(m, R, Q, n, Elist, char, signature):
	# m, Q, n, Elist, char as above
	# R is d*Q, this is Alice's public key
	# signature is the list [r, s] as above
	r = signature[0]
	s = signature[1]
	z = HashMessage(m, n)
	w = EC.invMod(s, n)
	w = w%n
	u1 = (z*w)%n
	u2 = (r*w)%n
	u1Q = EC.nP(u1, Q, Elist, char)
	u2R = EC.nP(u2, R, Elist, char)
	T = EC.addPts(u1Q, u2R, Elist, char)
	
	return ( (T[0])%n == r%n)


# log n number of bits 
