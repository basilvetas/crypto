# pow(239587, 992743, 58234)
# 
# 3) Python is able to use the pow() function to do quick claculations of large exponents by
#			bit manipulation??
#			(a * b * c) mod n = ((a * b) mod n) * c) mod n	
# 


# Returns a list of prime factors of the parameter n
def factor(n):
	myList = []
	i = 2
	while((n > 1) and (i**2 < n + 1)):		
		
		if((n % i) == 0):
			myList.append(i)
			n = n / i
		else:
			i = i + 1

	if (i**2 > n):
		myList.append(n)
	return myList

# Returns a list of unique prime factors from our factor list
def uniqueFactors(factors):
  unique = []
  for x in factors:
    if x not in unique:
      unique.append(x)
  return unique

# Checks if param a is a primitive root mod a prime param p
def isPrimitiveRoot(a, p):
	s = p - 1
	uniqFactors = uniqueFactors(factor(s))
	i = 0
	while(i < len(uniqFactors)):
		exp = s / uniqFactors[i]
		if(pow(a, exp, p) == 1):
			return False		
		i = i + 1

	return True

# Finds primitive root for prime param p
def findPrimitiveRoot(p):
	i = 2
	while (i < p):
		if(isPrimitiveRoot(i, p)):
			return i
		i = i + 1



# Solves for n in equation a^n = b mod p 
def discreteLog(a, b, p):
	if (isPrimitiveRoot(a, p)):
		i = 1
		while(i < p):
			if(pow(a, i, p) == b):
				return i
			i = i + 1 


# Test Primes
# p = 60077, a = 2 b = 71, n = 46067 (fast)
# p = 528763, a = 2, b = 71, n = 466434 (fast)
# p = 9326077, a = 5, b = 71, n = 2638103 (fast)
# p = 148256399, a = 7, b = 71, n = 53762400 (slow)
# p = 2994528541, a = 6, b = 71, n = ?? (too slow I gave up)
# p = 67942202161, a = 31
# p = 2851905084269, a = 2
# p = 199962421245781, a = 6












