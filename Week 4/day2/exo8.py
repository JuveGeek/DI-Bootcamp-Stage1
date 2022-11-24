pizza=input("Entrez la garniture de pizza ? : ")
pie=[]
pie.append(pizza)

while pizza != "quit":
    print("\n Vous ajouterez une garniture de pizza !")
    pizza=input("Entrez la garniture de pizza ? : ")
    pie.append(pizza)

print("L'ensemble donne : ",pie)

tot=len(pizza)
total= int(tot)

print("\n Prix total est : ", total*2.5+10)