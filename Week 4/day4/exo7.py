from random import *

def get_random_temp(season):
    if season=="winter":
        return randint(-10, 16)
    elif season=="spring":
        return randint(17, 32)
    elif season=="summer":
        return randint(33,42)



def main():

    seas=input("Quelle est la saison : ")

    temp=get_random_temp(seas)
    print("The temperature right now is {} degrees Celsius.".format(temp))

    if temp<0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif temp<16:
        print("Quite chilly! Don’t forget your coat")
    elif temp<32:
        print("It's warming up !")
    else:
        print("Too hot, dont go out !!")
    

main()