# Basil Vetas
# 9/23/16

# Computes kth element in union of A and B in O(logn + logm) time
# A of size n
# B of size m
# k
def findKthElement(A, B, n, m, k):  
  if(k == 1):
  	return min(A[k-1], B[k-1])
  
  if(n == 0 and m > 0):
  	return B[k]

  if(n < k/2):
  	i = n
  else:
  	i = k/2  	

  if(m < k/2):
  	j = m
  else:
  	j = k/2  	

  if(A[i-1] > B[j-1]):
  	m = m - j
  	k = k - j
  	return findKthElement(A[:], B[j:], n, m, k)

  if(A[i-1] < B[j-1]):
  	n = n - i
  	k = k - i
  	return findKthElement(A[i:], B[:], n, m, k)








