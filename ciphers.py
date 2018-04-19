import string

def rot13(message, rot):
	
	'''Implementation of the ROT13 Cipher using ASCII Decimal Values'''

	encryptedMsg = ''

	for char in message:

		count = rot

		if " " in char:
			encryptedMsg += ' '

		# Capital Letters
		elif ord(char) >= 65 and ord(char) <= 90:
			if ord(char) + count > 90:
				diff = 90 - ord(char)
				count = count - diff
				encryptedMsg += chr(65 + (count - 1))
			else:
				encryptedMsg += (chr(ord(char) + rot))
		# Lowercase Letters
		elif ord(char) >= 97 and ord(char) <= 122:
			if ord(char) + count > 122:
				diff = 122 - ord(char)
				count = count - diff
				encryptedMsg += chr(97 + (count - 1))
			else:
				encryptedMsg += (chr(ord(char) + rot))
		# Special Characeters
		else:
			encryptedMsg += char
			
	return encryptedMsg

def rot47(message, rot):
	'''Implementation of the ROT47 Cipher using ASCII Decimal Values 33-126'''

	encryptedMsg = ''

	for char in message:

		count = rot

		if " " in char:
			encryptedMsg += ' '
		
		elif ord(char) in range(33, 127):
			if ord(char) + count > 126:
				diff = 126 - ord(char)
				count = count - diff
				encryptedMsg += chr(33 + (count - 1))
			else:
				encryptedMsg += (chr(ord(char) + rot))
		else:
			encryptedMsg += char

	return encryptedMsg

def caesarCipher(message, shift):
	'''Implementation of the Caeser Cipher'''

	if shift % 26 == 0:									# Raise error if shift won't work
		raise ValueError("Shift value will not encode text")

	message = message.lower().replace(" ", '')			# Remove spaces in message
	alphabet = string.ascii_lowercase					# Create list of alphabet
	shiftAlphabet = alphabet[shift:] + alphabet[:shift]	# Create shifted list

	hiddenMsg = ''

	for x in range(0, len(message)):
		for y in range(0, len(alphabet)):
			if message[x] == alphabet[y]:				# If index in alphabet = letter in msg
				hiddenMsg += shiftAlphabet[y]			# Use that index in shifted alphabet

	return hiddenMsg

