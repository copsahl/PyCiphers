from ciphers import *
from os import system
from time import sleep

def menu():

	option = ''
	system("cls || clear")

	print('''
    ____        _______       __             
   / __ \__  __/ ____(_)___  / /_  ___  _____
  / /_/ / / / / /   / / __ \/ __ \/ _ \/ ___/
 / ____/ /_/ / /___/ / /_/ / / / /  __/ /    
/_/    \__, /\____/_/ .___/_/ /_/\___/_/     
      /____/       /_/                       
		''')

	print("Pick a cipher/encoding function:")
	print("\t- Caesar Cipher(cc)\t- Morse Code(mc)")
	print("\t- ROT13(r13)")
	print("\t- ROT47(r47)")
	print("\t- Affine Encode(ae)")

	while True:

		option = input(">")
		if option == 'exit':
			return 0

		message = input("Enter message: ").lower()

		if 'cc' in option.lower():
			shift = eval(input("How many shifts: "))
			try:
				newMsg = caesarCipher(message, shift)
			except:
				print("Shift 26 doesn't encode message. Try a different number!")
		elif 'r13' in option:
			rot = eval(input("How many rotations: "))
			newMsg = rot13(message, rot)
		elif 'r47' in option:
			rot = eval(input("How many rotations: "))
			newMsg = rot47(message, rot)
		elif 'ae' in option.lower():
			aKey = eval(input("Enter 'A' Key: "))
			bKey = eval(input("Enter 'B' Key: "))
			newMsg = affineEncode(message, aKey, bKey)
		elif 'mc' in option:
			decode = input("Encode(e) or Decode(d): ").lower()
			if decode == 'e':
				newMsg = morseCode(message, False)
			elif decode == 'd':
				newMsg = morseCode(message, True)
			else:
				print("Invalid Option...")
			
		print("New message: {}".format(newMsg))

if __name__ == '__main__':
	menu()
