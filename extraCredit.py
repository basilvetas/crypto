# Basil Vetas
# 3/15/16

# Quadratic Sieve Implementation (dumb version)
    
# integer square root (floored)
def isqrt(n):
  x = n
  y = (x + 1) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

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

  # once we know the prime factors we need to find y
  for f in factor_map:    
    temp = factor_map[f]
    temp_f = f

    # reduce the power to 2 for all factors
    while (temp > 2):
      temp_f *= f
      temp -= 2
    del factor_map[f]
    factor_map[temp_f] = 2
    
  # get y by multiplying each factor we have left in our map
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


