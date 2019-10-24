

#function for addition
def add():
    firstNum = float(input())
    secondNum = float(input())
    sumNumbers = firstNum + secondNum
    print(sumNumbers)

#function for subtraction
def subtract():
    firstNum = float(input())
    secondNum = float(input())
    difference = firstNum - secondNum
    print(difference)

#function for multiplication
def multiplication():
    firstNum = float(input())
    secondNum = float(input())
    product = firstNum * secondNum
    print(product)

#function for division
def division():
    firstNum = float(input())
    secondNum = float(input())
    quotient = firstNum / secondNum
    print(quotient)

#Temperature conversions

#Celcius to Fahrenheit
def celciusFahrenheit():
    print("Enter Celcius Degrees: ")
    c_read = input()
    c_float = float(c_read)   
    celcius =  float(c_float * 1.8 + 32.0)
    print(str(celcius) + " Degrees Fahrenheit!")

#Fahrenheit to Celcius
def fahrenheitCelcius():
    print("Enter Fahrenheit Degrees: ")
    f_read = input()
    f_float = float(f_read)
    fahrenheit =  float((f_float - 32.0) * 5/9)
    print(str(fahrenheit) + " Degrees Celcius!")

#Prints command interface
print("Welcome to my basic 4 Function Calculator!                ")
print("What would you like to calculate today?                   ")
print("These are your options! Add, Subtract, Multiply or Divide ")
print("For tempertature conversions type f to c or c to f.       ")
print("--------------------------------------------------------- ")
task = input()

#If statements that run certain functions if key is inputed
if task == "multiply":
    multiplication()
elif task == "add":
    add()
elif task == "subtract":
    subtract()
elif task == "divide":
    division()
elif task == "c to f":
    celciusFahrenheit()
elif task == "f to c":
    fahrenheitCelcius()
else:
    print("Enter a valid operation that is provided!")

