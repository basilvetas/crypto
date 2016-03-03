# Basil Vetas
# February 28, 2016

# Implementation of the 'p - 1' and 'p + 1' factorization 
# schemes for finding large primes


### p - 1 Implementation ###

# A function that takes the number 'n' we want to factor,
# then does the 'p-1' test based on a user-specified 'a'
import fractions

def pMinusOne(n, a):
	d = fractions.gcd(a, n)
	if (d > 1):
		return d

	ai = a
	i = 2
	while (True):
		ai = pow(ai, i, n)

		if(ai == 1):
			return n

		d = fractions.gcd(ai - 1, n)

		if (d > 1):
			return d
		else:
			i += 1

# Runs 'p - 1' method on number 'n' for a series of 'a' values
def finalpMinusOne(n):
	a = 2
	d = n
	while ((d == n) and (a < n)):
		d = pMinusOne(d, a)
		a += 1
	return d


### p + 1 Implementation ###


# A function that takes two polynomials and computes
# them as (a + b*sqrt(d))*(c + e*sqrt(d)) = (ac + bed) + (ae + bc)
def prodElts(ll1, ll2, d, m):
	a = ll1[0]
	b = ll1[1]
	c = ll2[0]
	e = ll2[1]	
	return [ (a*c + b*e*d)%m, (a*e + b*c)%m]

# A function that computes the 'mth' power of (a + b*sqrt(d)) by 
# takes in [a,b], d, m and outputs a list [a', b'] (SLOW VERSION)
def powOfAPlusBSqrtDSlow(ll, m, d, n):	
	i = 1
	curll = ll
	while(i < m):
		curll = prodElts(curll, ll, d, n)
		i += i

	return curll

# A function that computes the 'mth' power of (a + b*sqrt(d)) by 
# takes in [a,b], d, m and outputs a list [a', b'] (FAST VERSION)
def powOfAPlusBSqrtD(ll, m, d, n):	
	if(m == 0):
		return [1, 0]
	elif (m == 1):
		return ll
	elif (m == 2):
		return prodElts(ll, ll, d, n)
	else:
		ll1 = powOfAPlusBSqrtD(ll, m%2, d, n)
		ll2 = powOfAPlusBSqrtD(powOfAPlusBSqrtD(ll, m//2, d, n), 2, d, n)		
		return prodElts(ll1, ll2, d, n)

# A function that takes the number 'n' we want to factor,
# then does the 'p+1' test based on a user-specified 'z' and 'd'
def pPlusOne(n, z, d):
	normZ = prodElts(z, [z[0], (-1)*z[1]], d, n)

	mygcd = fractions.gcd(normZ[0], n)
	if (mygcd > 1):
		return mygcd

	zi = z
	i = 2

	while (True):
		zi = powOfAPlusBSqrtD(zi, i, d, n)
		
		mygcd = fractions.gcd(zi[1], n)

		if(mygcd == n):
			return n

		if(mygcd > 1):
			return mygcd
		else:
			i += 1


