"""
Ceasercipher, by Booked or 7OID,
Just a funny test, you can use these functions to create a vigenere ciphere.
"""



"""
This function takes text, and converts it into a list, it also converts all letters in the string to captial letters
"""
def convert(x):
	listt = []
	listt[:0] = x.upper()
	return listt

"""
This is the main function of the program, it takes a string, it replaces the spaces between the text,  then 
convers it into a list. Then it uses an algorithm to convert each of letters in the string, using a table of 
all the letters to derive the number of the letter. Then, it uses x the key, as the cipher, then it uses the 
index, and it adds the key, to the index, after that it shifts the numbers back into text, and it becomes 
ciphered using the key.
"""
def caesercipher(x,z):
	base = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	v = x.replace(' ','')
	xt = convert(v)
	ide = len(xt)
	list1 = []
	for i in range(ide):
		F = base.index(xt[i])
		list1.append(F)
	list2 = list1.copy()
	cipher = z
	for a in range(ide):
		h = list2[a] + cipher
		if h >= 25:
			h -= 26
		list2[a] = base[h]
	string1 = ''.join(map(str,list2))
	return(string1)
	list2 = list1.copy() 

"""
The brute force decrypt function basically uses brute force to test all the possible keys in the alphabet, which 
is 25, and the ciphered text itself, then it uses the ceasercipher function to brute force decrypt.
"""
def bruteforcedecrypt(y):
	for h in range(26):
		print(caesercipher(y,h))

"""
Option 1 is when the user chooses to encrpyt, it asks them what they wanna encrpyt and what key it uses.
"""
def option_1():

	useri1 = str(input("Enter something that you'd like to cipher:  "))

	useri2 = int(input("Enter the amount of times that you want to cipher the text, 1-25:  "))

	if useri2 > 25:
		while useri2 > 25:
			useri2 = int(input("Enter the amount of times that you want to cipher the text, 1-25:  "))
			if useri2 <=25:
				break
	
	print("Here is your ciphered text!:  " + caesercipher(useri1,useri2))

"""
Option 2 is when the user chooses to decrpyt, it will ask them what's the encrypted text, and will use the 
bruteforcedecrypt function to perform this.
"""
def option_2():
	
	useri1 = str(input("Please enter in ciphered text:  "))
	print("You will find your deciphered text in this list!")
	bruteforcedecrypt(useri1)
	
useri3 = str(input("Would you like to encrypt or decrypt text, - encrypt - decrypt:  "))

useri3 = useri3.lower() # This converts the users input from the question to lower case characters


"""
This piece of code basically decides between the two options, and if the user doesn't choose either encrypt or 
decrypt, they will be asked the question again.
"""
if useri3 != 'encrypt':
	if useri3 != 'decrypt':
		while useri3 != 'encrypt' or useri3 != 'decrypt':
			if useri3 == 'encrypt' or useri3 == 'decrypt':
				break
			useri3 = str(input("Would you like to encrypt or decrypt text, - encrypt - decrypt:  "))
			useri3 = useri3.lower()
			if useri3 == 'encrypt' or useri3 == 'decrypt':
				break

# This finally gives checks the decision and runs the functions.
if useri3 == 'encrypt':
	option_1()
else:
	option_2()
