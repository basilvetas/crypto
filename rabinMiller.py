# Basil Vetas
# 2/18/16

# A function which figures out how many powers of 2 divide a number
def power2Count(n):
	i = 0
	while (n%2 == 0):
		n = n/2
		i += 1
	return [i, n]

#  A function which checks if a particular number a proves that n is composite (via Rabin-Miller).
#  Returns True is the number is composite, and returns False if the test is inconclusive
def RMCompositeTest(a, n):
	shortList = power2Count(n-1)
	k = shortList[0]
	q = shortList[1]
	# note then that n-1 = 2^k * q
	if(pow(a,q,n) == 1):
		return False

	for i in range(0, k):
		if(pow(a,pow(2,i)*q, n) == n-1):
			return False

	return True

import random

# A function that will generate K random a values and check them all to see if n is proved composite
def runRMKTimes(K, n):
	for j in range(0, K):
		a = random.randint(2, n-1)

		if(RMCompositeTest(a, n)):
			return True
		
	return False


# A function that finds the next number that is probably prime after a given number
# Pass a number C and the number n
# Try to find the next prime after n by doing C Rabin-Miller tests
def findNextPrime(C, n):
	n = n + 1 # go to the next number to see if it could be prime
	if(n%2 == 0):
		n = n + 1 # if n is even, make it odd, we will increment by 1		
	
	while(True):
		if not runRMKTimes(C, n):
			return n
		n = n + 2		




