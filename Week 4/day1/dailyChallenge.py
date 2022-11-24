import random

chaine= input("Entrer une chaçine de caractère (10 caractaire) : ")

if len(chaine) >10:
    print("La chaine est trop longue")
elif len(chaine)<10:
    print("La chaine est trop courte")
print("Le premier caractère est : "+chaine[0])
print("Le dernier caractère est : "+chaine[-1])

for i in range(len(chaine)):
    print(chaine[:i+1])

print("La chaine de caractère renversée est : "+''.join(random.sample(chaine,len(chaine))))