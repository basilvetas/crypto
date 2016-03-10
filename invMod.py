# Basil Vetas
# 3/9/16

# Computes 'a' modulo 'n'
def invMod(a,n):
  #this finds the inverse of a mod n
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

# RSA Encryption and Decryption Implementation

# Encrypts plaintext 'x' using RSA where (m, e) is the public key
# Outputs x^e mod m
def RSAencrypt(x, m, e):  
  return pow(x, e, m)

# Decrypts ciphertext 'y' using RSA where m = p*q

def RSAdecrypt(y, p, q, e):
  # first need to find d = e^(-1) mod fi(m)
  euler_fi = (p - 1)*(q - 1)
  d = invMod(e, euler_fi) % euler_fi  
  m = p*q
  plaintext = pow(y, d, m)
  return plaintext

# Make a couple large primes, choose a decent size e, and then try encrypting and decrypting



# Quadratic Sieve Implementation (dumb version)
    
# integer square root (floored)
def isqrt(n):
  x = n
  y = (x + 1) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

# , maxi=-1
def poorQuadSieve(n):
  #this looks for numbers x such that x^2 mod n is a perfect square...
  sqrtN = isqrt(n)
  i = 1
  factoredFlag = False
  factor_map = {} # a list of prime factors mapped to their powers
  x = 0

  while (factoredFlag == False):
    a = sqrtN + i
    a_sq = pow(a, 2, n)
    prime_factors = factor(a_sq)  
    x = a

    # check if list is has even number
    if((len(prime_factors) % 2) == 0 ):
      count = 0
      current = prime_factors[0]
      other_count = 0
      # for each prime factor, check if there are an even number of that power in the list
      for j in prime_factors:
        other_count += 1
        # increment for matches        
        if(current == j):
          count += 1          
        else: # otherwise check if we have an even number and move to the next prime factor
          if((count % 2) == 0):
            factor_map[current] = count 
            # print "factor_map", factor_map            
            # factoredFlag = True
            count = 1
            current = j  # move to the next prime factor
          else: # if not an even count, we can stop and move to the next number to check                        
            break

      # at the end of the for loop if our last count is even, we are done factoring
      if((count % 2) == 0):
        factor_map[current] = count 
        factoredFlag = True
          
    i = i+1

  for f in factor_map:    
    temp = factor_map[f]
    temp_f = f
    while (temp > 2):
      temp_f *= f
      temp -= 2
    del factor_map[f]
    factor_map[temp_f] = 2
    
  y = 1;
  for g in factor_map:
    y *= g

  factor_one = x - y
  factor_two = x + y

  return [factor_one, factor_two]


# Helper function for factoring
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






