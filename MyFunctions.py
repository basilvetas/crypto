# Basil Vetas
# January 14, 2016

# import MyFunctions
# MyFunctions.IsThree(n)
# MyFunctions.gcd(s,t)

def IsThree(n):
	if(n == 3):
		print("the number is 3")
		return True
	else:
		print("the number is not 3")
		return False

def gcd(s,t):	
	if(s > t):
		a = s
		b = t
	else:
		a = t
		b = s
	q = a/b
	r = a%b	
	print (a,q,b,r)
	if(r == 0):
		print b
		return (a,q,b,r)
	else:
		gcd(b,r)

# def bezout(a,b):
	
