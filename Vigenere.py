# Basil Vetas
# January 21, 2016

# import Vigenere
# Vigenere.Encrypt('key', 'plaintext')

def Encrypt(key, plaintext):
	import string
	key = key.upper()
	codeList = [ord(c)-ord('A') for c in key]
	codeLen = len(key)
	plaintext = plaintext.upper()
	textLen = len(plaintext)
	plainlist = [ord(c) - ord('A') for c in plaintext]
	for i in range(0,textLen):
		plainlist[i] += codeList[i%codeLen]
		plainlist[i] %= 26
	plainlist = [i + ord('A') for i in plainlist]
	encryptedText = [chr(i) for i in plainlist]
	return ''.join(encryptedText)

def Decrypt(key, ciphertext):
	import string
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




