
# Computes 'a' modulo 'n'
### BROKEN
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

# RSA Encryption and Decryption Implementation

# Encrypts plaintext 'x' using RSA where (m, e) is the public key
# Outputs x^e mod m
def RSAencrypt(x, m, e):
  ciphertext = pow(x, e, m)
  return ciphertext

# Decrypts ciphertext 'y' using RSA where m = p*q

def RSAdecrypt(y, p, q, e):
  # first need to find d = e^(-1) mod fi(m)
  euler_fi = (p - 1)*(q - 1)
  d = invMod(e, euler_fi)  
  m = p*q
  plaintext = pow(y, d, m)
  return plaintext

# Make a couple large primes, choose a decent size e, and then try encrypting and decrypting



# Quadratic Sieve Implementation (dumb version)
    
















