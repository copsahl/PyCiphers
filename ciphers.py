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

'''Affine Cipher'''
affineDic = string.ascii_uppercase

def affineEncode(message, aKey, bKey):
	'''Implementation of the affine cipher'''

	global affineDic

	message = message.upper()
	charValues = []
	encodedMsg = ''

	for char in message:
		for val in range(0,len(affineDic)):
			if char == affineDic[val]:
				charValues.append(val)

	for value in charValues:
		num = ((aKey * value) + bKey) % 26
		for val in range(0, len(affineDic)):
			if num == val:
				encodedMsg += affineDic[val]
	return encodedMsg


def morseCode(message, decode):
	'''Implementation of Morse Code'''

	morseDic = {

		'A':'.-',
		'B':'-...',
		'C':'-.-.',
		'D':'-..',
		'E':'.',
		'F':'..-.',
		'G':'--.',
		'H':'....',
		'I':'..',
		'J':'.---',
		'K':'-.-',
		'L':'.-..',
		'M':'--',
		'N':'-.',
		'O':'---',
		'P':'.--.',
		'Q':'--.-',
		'R':'.-.',
		'S':'...',
		'T':'-',
		'U':'..-',
		'V':'...-',
		'W':'.--',
		'X':'-..-',
		'Y':'-.--',
		'Z':'--..',
		'1':'.----',
		'2':'..---',
		'3':'...--',
		'4':'....-',
		'5':'.....',
		'6':'-....',
		'7':'--...',
		'8':'---..',
		'9':'----.',
		'0':'-----',
		'.':'.-.-.-',
		',':'--..--',
		'?':'..--..',
		'/':'-..-.',
		'@':'.--.-.',
		' ':'/'
	}

	message = message.upper()
	encodedMsg = ''

	if decode == False:

		for char in message:
			for k,v in morseDic.items():
				if char == k:
					encodedMsg += (str(v) + " ")

	elif decode == True:
		if '/' in message:
			words = message.split(" / ")
			for x in range(0, len(words)):
				letters = words[x].split(" ")
				for x in range(0, len(letters)):
					for k, v in morseDic.items():
						if letters[x] == v:
							encodedMsg += k
				encodedMsg += " "

		else:
			letters = message.split(" ")
			for x in range(0, len(letters)):
				for k,v in morseDic.items():
					if letters[x] == v:
						encodedMsg += k

	return encodedMsg
