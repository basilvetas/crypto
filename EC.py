# Basil Vetas
# 4/7/16

# Adding and Doubling Elliptic Curve Math!
# We always assume our elliptic curve is written as y^2 = x^3 + ax^2 + bx + c
# Link below has a good example problem that I used for testing values of nP
# http://crypto.stackexchange.com/questions/3907/how-does-one-calculate-the-scalar-multiplication-on-elliptic-curves

# Note, if char is 0, we should use for our point:
from fractions import Fraction
# Fraction(1,2) + Fraction(1,3)

# A function that checks whether a point [x,y] lies on the elliptic curve specified by the values [a,b,c]
def isPtOnC(P, Elist, char):
  x = P[0]
  y = P[1]
  a = Elist[0]
  b = Elist[1]
  c = Elist[2]

  if(char > 0):
  	x = x%char
  	y = y%char

  y_val = pow(y,2)
  x_val = pow(x,3) + a*pow(x,2) + b*x + c

  if(char > 0):
  	y_val = y_val%char
  	x_val = x_val%char

  if(y_val == x_val):
  	return True
  else:
  	return False


# A function which doubles a point, ie computes P + P = 2P
def doublePt(P, Elist, char):
  x = P[0]
  y = P[1]
  a = Elist[0]
  b = Elist[1]
  c = Elist[2]
  inf = float("inf")
  if (y == inf): # first handle the case if we are doubling the point at infinity
      return [float("inf"), float("inf")]
  if (char > 0 and y%char == 0): # next handle the case if our tangent line is vertical
    return [float("inf"), float("inf")]
  # now do the real work, remember
  # A = (3x^2 + 2ax + b)/(2y), so we need to invert 2y
  A = 0

  if (char > 0):  # first do the positive characteristic case
  	twoyinv = invMod(2*y, char)
  	twoyinv = twoyinv%char
  	A = (3*pow(x,2) + 2*a*x + b)*(twoyinv)
  	A = A%char
  else:  	
  	A = Fraction(3*pow(x,2) + 2*a*x + b, 2*y)
  
  new_x = pow(A,2)-a - 2*x
  new_y = A*(x-new_x) -y

  if(char > 0):
  	new_x = new_x%char
  	new_y = new_y%char

  return [new_x, new_y]


# A function that adds two arbitrary points on the elliptic curve.
def addPts(P, Q, Elist, char):
	xP = P[0]
	yP = P[1]
	xQ = Q[0]
	yQ = Q[1]

	# if points are the same, double them
	if((xP == xQ) and (yP == yQ)):
		return doublePt(P, Elist, char)

	a = Elist[0]
	b = Elist[1]
	c = Elist[2]
	inf = float("inf")
	#first we handle all the easy cases
	if (yP == inf):
		return Q
		if (yQ == inf):
			return P
		if (xP == xQ):
			if (yP == yQ):#if we are doubling a point...
				return doublePt(P, Elist, char)
			else: #if we are not doubling a point, but the x-coords
				#agree, then we are going to add to infinity.
				return [float("inf"), float("inf")]
	#next do the real work.
	A = 0
	if (char > 0):  #do the positive characteristic case
		deltaXinv = invMod(xQ - xP, char)
		deltaXinv = deltaXinv%char
		A = (yQ - yP)*deltaXinv
		A = A%char
	else: 
		A = Fraction(yQ - yP, xQ - xP)


	new_x = pow(A,2)-a - xP - xQ
	new_y = A*(xP - new_x) - yP

	if(char > 0):
		new_x = new_x%char
		new_y = new_y%char

	return [new_x, new_y]


# Calculates nP (adds P to itself n times)
def nP(n, P, Elist, char):
	i = 1
	while(i < n/2 + 1):	# double i until we would exceed n
		i *= 2

	rem = n - i # get the remainder after doubling
	doubles = nPdouble(n, P, Elist, char)	# double recursively until we can't

	if(rem == 0):	# if remainder is zero, we are done
		return doubles
	else:	# otherwise, add P 'rem' more times with recursion
		return addPts(doubles, nP(rem, P, Elist, char), Elist, char)


# Helper method that doubles P n times recursively
def nPdouble(n, P, Elist, char):
	if(n == 1):
		return P
	else:	# recursively doubles nP as many times as possible
		return nPdouble(n/2, doublePt(P, Elist, char), Elist, char)	

# A naive discrete log function for elliptic curves. 
# In other words, given Q = nP, this loops and finds the value n.
def disLogEC(Q, P, Elist, char):
	xP = P[0]
	yP = P[1]
	xQ = Q[0]
	yQ = Q[1]
	n = 0
	while(xP != xQ or yP != yQ):
		n += 1
		xP, yP = nP(n, P, Elist, char)
		
	return n

# Finds the inverse of a mod n
def invMod(a,n):
  r1 = n
  r2 = a
  tempR = 0
  t1 = 0
  t2 = 1
  tempT = 0
  q = 0
  while (r2 > 0):
    q = r1//r2
    tempT = t2
    t2 = t1 - q*t2
    t1 = tempT
    tempR = r2
    r2 = r1 - q*r2
    r1 = tempR
  if (r1 > 1):
    return 0
  return t1

# A class that represents a point on an elliptic curve
# Constructor takes two lists: One defininf a point, and one
# defining an eliptic curve. It also takes an integer--char. 
# If char is zero, no modular arithmetic is used. Otherwise
# everything is mod <char>.
class ECPt:
	def __init__(self, P, Elist, char):		
		if(isPtOnC(P, Elist, char)):
			self.pt = P
			self.EC = Elist
			self.ch = char
		else:
			print "P is not a point on the specified Elliptic Curve, try again."
				
	# Override reverse add
	def __add__(self, Q):
		if(isPtOnC(Q.pt, self.EC, self.ch)):						
			return ECPt(addPts(self.pt, Q.pt, self.EC, self.ch),self.EC, self.ch)
		else:
			print "these points are not on the same elliptic curve"    

	def __mul__(self, n):
		return ECPt(nP(n, self.pt, self.EC, self.ch), self.EC, self.ch)

	def __rmul__(self, n):
		return ECPt(nP(n, self.pt, self.EC, self.ch), self.EC, self.ch)



