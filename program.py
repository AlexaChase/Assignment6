import random
def formula(n):
    value= 0
    for i in range(n):
        calculation= (-1) ** i /(2*i+1)
        value= value + calculation
    return value*4

iterations= input("Please enter 'select' to let the program choose a number or enter 'number' to choose your own: ")
if iterations == "number":
    number= int(input("Please enter a number: "))
    pi=formula(number)
    print("The value of pi is:", pi)
if iterations== "select":
    number= random.randint(1, 100)
    print("The value selected by the program is:", number)
    pi=formula(number)
    print(pi)
else:
    print("Error, please try again")
    
