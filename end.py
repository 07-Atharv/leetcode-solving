# Diffie-Hellman Code


def prime_checker(p):
	# Checks If the number entered is a Prime Number or not
	if p < 1:
		return -1
	elif p > 1:
		if p == 2:
			return 1
		for i in range(2, p):
			if p % i == 0:
				return -1
			return 1


def primitive_check(g, p, L):
	# Checks If The Entered Number Is A Primitive Root Or Not
	for i in range(1, p):
		L.append(pow(g, i) % p)
	for i in range(1, p):
		if L.count(i) > 1:
			L.clear()
			return -1
		return 1


l = []
while 1:
	P = int(input("Enter P : "))
	if prime_checker(P) == -1:
		print("Number Is Not Prime, Please Enter Again!")
		continue
	break

while 1:
	G = int(input(f"Enter The Primitive Root Of {P} : "))
	if primitive_check(G, P, l) == -1:
		print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
		continue
	break

# Private Keys
x1, x2 = int(input("Enter The Private Key Of User 1 : ")), int(
	input("Enter The Private Key Of User 2 : "))
while 1:
	if x1 >= P or x2 >= P:
		print(f"Private Key Of Both The Users Should Be Less Than {P}!")
		continue
	break

# Calculate Public Keys
y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# Generate Secret Keys
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

print(f"\nSecret Key For User 1 Is {k1}\nSecret Key For User 2 Is {k2}\n")

if k1 == k2:
	print("Keys Have Been Exchanged Successfully")
else:
	print("Keys Have Not Been Exchanged Successfully")


Output-
Enter P : 11
Enter The Primitive Root Of 11 : 2
Enter The Private Key Of User 1 : 8
Enter The Private Key Of User 2 : 4

Secret Key For User 1 Is 4
Secret Key For User 2 Is 4

Keys Have Been Exchanged Successfully

=== Code Execution Successful ===



# Python3 program to illustrate
# Rail Fence Cipher Encryption
# and Decryption
 
# function to encrypt a message
def encryptRailFence(text, key):
 
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix
    # to distinguish filled
    # spaces from blank ones
    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
     
    # to find the direction
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
         
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
# Driver code
if __name__ == "__main__":
    print(encryptRailFence("thisisasecretmessage", 2))
    print(encryptRailFence("thisisasecretmessage", 3))
    print(encryptRailFence("thisisasecretmessage", 4))







# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are
# relatively small compared to practical application

import math

def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp


p = 3
q = 11
n = p*q
e = 7
phi = (p-1)*(q-1)

while (e < phi):

	# e must be co-prime to phi and
	# smaller than phi.
	if(gcd(e, phi) == 1):
		break
	else:
		e = e+1

# Private key (d stands for decrypt)
# choosing d such that it satisfies
# d*e = 1 + k * totient

k = 1
d = (1 + (k*phi))/e

# Message to be encrypted
msg = 2.0

print("Message data = ", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)

# Decryption m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)





Message data =  2.0
Encrypted data =  29.0
Original Message Sent =  2.0

=== Code Execution Successful ===


pip install pycryptodome


from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext, tag)
print(f'Cipher text: {ciphertext}')
if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')




Output

Enter a message: hi
Cipher text: b'\x98%'
Plain text: hi






ASCII value of uppercase alphabets – 65 to 90. ASCII value of lowercase alphabets – 97 to 122.

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def main():
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift value for encryption: "))

    encrypted_text = caesar_encrypt(plaintext, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    print("\nOriginal Text:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()

Output-

enter the plaintext: hi
Enter the shift value for encryption: 3
Original Text: hi
Encrypted Text: kl
Decrypted Text: hi


# Python code to implement
# Vigenere Cipher

# This function generates the 
# key in a cyclic manner until 
# it's length isn't equal to 
# the length of original text
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	
# This function returns the 
# encrypted text generated 
# with the help of the key
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
	
# This function decrypts the 
# encrypted text and returns 
# the original text
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	
# Driver code
if __name__ == "__main__":
	string = "GEEKSFORGEEKS"
	keyword = "AYUSH"
	key = generateKey(string, keyword)
	cipher_text = cipherText(string,key)
	print("Ciphertext :", cipher_text)
	print("Original/Decrypted Text :", 
		originalText(cipher_text, key))

Ciphertext : GCYCZFMLYLEIM
Original/Decrypted Text : GEEKSFORGEEKS


# Python3 code to implement Hill Cipher

keyMatrix = [[0] * 3 for i in range(3)]

# Generate vector for the message
messageVector = [[0] for i in range(3)]

# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]

# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

# Following function encrypts the message
def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):

	# Get key matrix from the key string
	getKeyMatrix(key)

	# Generate vector for the message
	for i in range(3):
		messageVector[i][0] = ord(message[i]) % 65

	# Following function generates
	# the encrypted vector
	encrypt(messageVector)

	# Generate the encrypted text 
	# from the encrypted vector
	CipherText = []
	for i in range(3):
		CipherText.append(chr(cipherMatrix[i][0] + 65))

	# Finally print the ciphertext
	print("Ciphertext: ", "".join(CipherText))

# Driver Code
def main():

	# Get the message to 
	# be encrypted
	message = "ACT"

	# Get the key
	key = "GYBNQKURP"

	HillCipher(message, key)

if __name__ == "__main__":
	main()



# Python3 program to illustrate
# Rail Fence Cipher Encryption
# and Decryption
 
# function to encrypt a message
def encryptRailFence(text, key):
 
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix
    # to distinguish filled
    # spaces from blank ones
    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
     
    # to find the direction
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
         
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
# Driver code
if __name__ == "__main__":
    print(encryptRailFence("thisisasecretmessage", 2))
    print(encryptRailFence("thisisasecretmessage", 3))
    print(encryptRailFence("thisisasecretmessage", 4))







# Python3 implementation of 
# Columnar Transposition
import math
 
key = "HACK"
 
# Encryption
def encryptMessage(msg):
    cipher = ""
 
    # track key indices
    k_indx = 0
 
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
 
    # calculate column of the matrix
    col = len(key)
     
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
 
    # add the padding character '_' in empty
    # the empty cell of the matix 
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
 
    # create Matrix and insert message and 
    # padding characters row-wise 
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
 
    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1
 
    return cipher
 
# Decryption
def decryptMessage(cipher):
    msg = ""
 
    # track key indices
    k_indx = 0
 
    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
 
    # calculate column of the matrix
    col = len(key)
     
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
 
    # convert key into list and sort 
    # alphabetically so we can access 
    # each character by its alphabetical position.
    key_lst = sorted(list(key))
 
    # create an empty matrix to 
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
 
    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
 
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
 
    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
 
    null_count = msg.count('_')
 
    if null_count > 0:
        return msg[: -null_count]
 
    return msg
 
# Driver Code
msg = "wearethebest"
 
cipher = encryptMessage(msg)
print("Encrypted Message: {}".
               format(cipher))
 
print("Decryped Message: {}".
       format(decryptMessage(cipher)))



Output-
Encrypted Message: eteahswebret
Decryped Message: wearethebest


Playfair Cipher



key=input("Enter key")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: #storing key
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): #storing other character
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  #Encryption
    msg=str(input("ENTER MSG:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decrypt():  #decryption
    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")


—----------------------------------------------------------------------------------------------------------------------------



key=input("Enter key")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: #storing key
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): #storing other character
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  #Encryption
    msg=str(input("ENTER MSG:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decrypt():  #decryption
    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")

—-----------------------------------------------------------------------------------------------------------------------


