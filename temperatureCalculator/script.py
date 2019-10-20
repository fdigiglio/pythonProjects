#Prints the pop up in terminal for user to input
print("Enter F for Fahrenheit to Celcius, Enter C for Celcius to Fahrenheit, or Press Q to Quit: ")
x = input()

#fahrenheit to celcius
if x=="f":
    print("Enter Fahrenheit Degrees: ")
    f_read = input()
    f_float = float(f_read)
    fahrenheit =  float((f_float - 32.0) * 5/9)
    print(str(fahrenheit) + " Degrees Celcius!")

#celcius to fahrenheit
if x=="c":
    print("Enter Celcius Degrees: ")
    c_read = input()
    c_float = float(c_read)   
    celcius =  float(c_float * 1.8 + 32.0)
    print(str(celcius) + " Degrees Fahrenheit!")

if x=="q":
    quit()