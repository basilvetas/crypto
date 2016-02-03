# Basil Vetas
# January 21, 2016

# to run from terminal,
# 	import Vigenere
import string
import operator		

def stripNonLetters(text):    
  for c in text:
		i = ord(c)-ord("A")
		if((i > 25) or (i < 0)):
			text = text.replace(c,'')
  return text

def encrypt(key, plaintext):	
	key = key.upper()
	codeList = [ord(c)-ord('A') for c in key]	
	codeLen = len(key)
	plaintext = plaintext.upper()
	plaintext = stripNonLetters(plaintext)
	textLen = len(plaintext)
	plainlist = [ord(c) - ord('A') for c in plaintext]		
	for i in range(0,textLen):
		plainlist[i] += codeList[i%codeLen]
		plainlist[i] %= 26	
	plainlist = [i + ord('A') for i in plainlist]
	encryptedText = [chr(i) for i in plainlist]
	return ''.join(encryptedText)

def decrypt(key, ciphertext):
	key = key.upper()
	codeList = [ord(c)-ord('A') for c in key]
	codeLen = len(key)
	ciphertext = ciphertext.upper()
	textLen = len(ciphertext)
	cipherlist = [ord(c) - ord('A') for c in ciphertext]
	for i in range(0,textLen):
		cipherlist[i] -= codeList[i%codeLen]
		cipherlist[i] += 26
		cipherlist[i] %= 26
	cipherlist = [i + ord('A') for i in cipherlist]
	decryptedText = [chr(i) for i in cipherlist]
	return ''.join(decryptedText)


# autocorrelation
def countLineUps(text, shiftSize):	
	count = 0
	textLen = len(text)
	shiftList = [c for c in text]	
	for i in range(0, textLen):
		pos = (i + shiftSize) % textLen 
		shiftList[pos] = text[i]
		if(shiftList[pos] == text[pos]):
			count += 1	
	return count

def autocorrelation(text):
	results = {0:0}
	shifts = range(0, len(text))
	matches = range(0, len(text))
	for i in range(1, len(text)):				
		count = countLineUps(text, i)
		shifts[i] = i		
		matches[i] = count 
		results[i] = count
	return results


def breakVigenere(text, k):
	# k represents how many key lengths you want to try
	matches = autocorrelation(text)	
	sortedVals = sorted(matches.items(), key=operator.itemgetter(1), reverse = True)	
	potentialKeys = []
	for i in range(0, len(sortedVals)):	
		if(sortedVals[i][0] < k):	
			potentialKeys.append(sortedVals[i][0])

	print potentialKeys
	for i in range(0, k):	# length of potential keys				
		keyGuess = getKey(text, potentialKeys[i])
		decrypted = decrypt(keyGuess, text)
		print "using " + keyGuess + " as the key, the message decodes to:\n\n" + decrypted + "\n\nDoes this look correct?"  
		ans = raw_input("Enter Yes or No: ")
		if(ans == "Yes"):
			print "\n\nYour key is " + keyGuess
			return

	print "Could not find a key with length between 0 and " + str(k)	


def getKey(message, interval):
	alphabetFrequencies = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']
	keyGuess = ""
	for n in range(0, interval): #For 5 columns
	  freqAlph = {'A':0, 'B':0, 'C':0, 'D':0,'E':0,'F':0,'G':0,'H':0,'I':0, 'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0, 'R':0, 'S':0, 'T':0,'U':0, 'V':0, 'W':0,'X':0,'Y':0,'Z':0}	  	  
	  for i in xrange(n, len(message), interval): # Iterate through message	  	
	  	freqAlph[message[i]] += 1  # Collect frequencies	  	
	  	if (i + interval) > len(message):
	  		break
	  frequencies = sorted(freqAlph.items(), key=operator.itemgetter(1), reverse = True) 
	  freqLetters = [] # Ordered list of frequent letters (their ASCII values)
	  for l in frequencies:
	  	freqLetters.append(ord(l[0])-ord('A'))
	  differences = {0:0}
	  for j in range(0, len(freqLetters)):
	  	key = (freqLetters[j]-(ord(alphabetFrequencies[j])-ord('A')))%26
	  	if key in differences:
	  		differences[key] += 1
	  	else:
	  		differences[key] = 1
	  differencesSorted = sorted(differences.items(), key=operator.itemgetter(1), reverse = True)
	  letter = chr(differencesSorted[0][0]+ord('A'))
	  keyGuess += letter
	return keyGuess


