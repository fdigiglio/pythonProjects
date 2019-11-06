import random
import string

#Variables

print("Generate a strong password here!")
print("First type in the length of characters you want!")
print("Type weak, medium, or strong for a password to be outputed.")
userInput = input()
str(charLength) = userInput

if str(charLength) < 8 and str(charLength) > 18:
    print("Enter a values greater than 8 and less than 18.")
elif str(charLength) > 8 and str(charLength) < 18:
    print("Valid") 


#Function for Generating
def generator(charLength, char = string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.choice(char) for _ in range(charLength))
    
    

runGenerator = generator(charLength)

runGenerator


