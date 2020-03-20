# A python programme to generate a random password for the user.
# The user provides the length of the password, which must be a minimum of 6. 
# The program will return a password that has a random combination of letters, 
# numbers, and symbols.

import random
import math

def generate_password(length):
    #Draw a number randomly for each position in password. 
    # Uses ASCII table.
    i = 0
    password = ""
    
    while (i < length):
        rand = random.random()
        code = math.floor(rand * 89) + 33
        password += chr(code)
        i += 1
    return password


length = int(input("Please enter a password length: "))

print("Your password is: ", generate_password(length))

