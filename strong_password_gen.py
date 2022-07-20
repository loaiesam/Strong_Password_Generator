import string
import random

s1 = list(string.ascii_lowercase) # 30%
s2 = list(string.ascii_uppercase) # 30%
s3 = list(string.digits)          # 20%
s4 = list(string.punctuation)     # 20%

characters_numbers = input("How many characters for the password?: ")

# Check the input
while True:
    try:
        characters_numbers = int(characters_numbers)
        if characters_numbers < 6:
            print("you need at least 6 characters")
            characters_numbers = input("please enter the number again: ")
        else:
            break
    except:
        print("please enter numbers only")
        characters_numbers = input("How many characters for the password?: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_numbers * (30/100)) # 30%
part2 = round(characters_numbers * (20/100)) # 20%

password = []

for i in range(part1):

    # ascii_lowercase
    password.append(s1[i])

    # ascii_uppercase
    password.append(s2[i])

for i in range(part2):

    # digits
    password.append(s3[i])

    # punctuation
    password.append(s4[i])

# Shuffling
random.shuffle(password)

password = "".join(password[0:])

print(password)
