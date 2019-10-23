#Prints to console for user input

def add():
    sum = 0
    num = 0
    while num != -1:
        sum += num
        print("Enter numbers to add, type -1 to enter values") 
        num = float(input())    

    print(sum)  

def multiply():
    product = 0
    num = 0
    while num != -1:
        product = num * num
        print("Enter numbers to multiply, type -1 to enter values")
        num = float(input())

    print(product)

def subtraction():
    difference = 0
    num = 0
    while num != -1:
        difference -= num
        print("Enter numbers to subtract, type -1 to enter values")
        num = float(input())

    print(difference)

def division():
    quotient = 0
    num = 0
    while num != -1:
        quotient = num / num
        print("Enter numbers to divide, type -1 to enter values")
        num = float(input())

    print(quotient)



print("Welcome to my awesome calculator")

print("What would you like to calculate")
print("These are your options! Area of triangle, c to f, add, sub, divide, multiply")
task = input()

if task == "multiply":
    multiply()
elif task == "add":
    add()
elif task == "subtract":
    subtraction()
elif task == "divide":
    division()
else:
    print("Enter a valid operation!")

