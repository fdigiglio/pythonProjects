import random

guesses = 0
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100!")

number = random.randint(1, 100)

while guesses < 15:
    
    if guesses < 1:
        print("You can now take an attempt at the number I am thinking of.")
    guess = input()
    guess = int(guess)

    guesses += 1
    if guesses >= 1:
        print("Take another shot!")

    if guess > number:
        print("Your number is to high!")
    if guess < number:
        print("Your number is too low!")
    if guess == number:
        break

if guess == number:
        print("Congratulations you have guess the correct number " + str(number))

if guess != number and guesses == 15:
        print("Looks like you ran out of turns. The number was " + str(number) + " !")

