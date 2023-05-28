import random
def formula(n):
    value= 1
    for i in range(n):
        calculation= (-1) ** i /(2*i+1)
        value= value + calculation
    return calculation*4

iterations= input("Please enter a number or select:")
if iterations== "select":
    number= random.randint(1, 100)
    print("The value selected by the program is:", number)
    pi=formula(iterations)
    print(pi)
if iterations== int():
    pi=formula(iterations)
    print("The value of pi is: ", pi)
