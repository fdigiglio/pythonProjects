#Prints to console for user input
# print("Enter which operation to continue ( *, /, +, - ): ")
# x = input()



# if x=="*":
#     print("Print numbers you want to multiply: ")
#     firstNum = input()
#     secondNum = input() 
#     float(firstNum) * float(secondNum)


    




def add():
    sum = 0
    num = 0
    while num != -1:
        sum += num
        print("Enter numbers to add, enter -1 to exit") 
        num = float(input())    

    print(sum)  






print("Welcome to my awesome calculator")

print("What would you like to calculate")
print("Area of triangle, c to f, add, sub, divide, multiple")
task = input()

if task == "Area of triangle":
    areaOfTriangle()
elif task == "add":
    add()