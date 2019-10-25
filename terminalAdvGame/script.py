
playerLives = 5

print("Welcome to the Terminal Adventure Game!")
print("Controls for Yes is y and for No is n! ")
print("---------------------------------------")

decision = input()

def firstLevel():
    print("Welcome to Colombia where the date is, October 24, 1986. \n You are an employee for Mr. Escobar but are not sure to report him to the police. \n You are receiving a phone call now from him.")
    print("Type yes to pick up the phone, no to hangup.")

def secondPrompt():
    decision

#while playerLives > 0:
    
if decision == "begin":
    firstLevel()
    if decision == "yes":
        secondPrompt()