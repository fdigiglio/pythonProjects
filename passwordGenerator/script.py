import string
string.ascii_letters
import random
#Variables
number = 0
password = ""
def letterGeneration():
    randomLetter = random.choice(string.ascii_letters)
    return randomLetter

print("Enter the amount of characters you want your password:")
userInput = input()
userInput = int(userInput)

while number < userInput:
    number += 1
    password = password + letterGeneration()

print("Your password is...", password)


