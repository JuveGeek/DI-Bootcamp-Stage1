from random import *

x = randint(1, 100)    # Pick a random number between 1 and 100.

def functionNumber(number):
    if (number == x):
        print("success message !!! ")
    else:
        print("fail message !!! \n")
        print("Generated number is : {} and entered number is : {} ".format(x,number))

functionNumber(20)