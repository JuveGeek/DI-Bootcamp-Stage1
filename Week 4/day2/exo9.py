askedAge=input("Entrez l'age de chaque person de la famille qui veut un ticket (Séparer chaque age par un seul espace) : ")
listAge=askedAge.split()

moinsTrois=0
troisDouz=0
plusDouz=0
moinsTroisTot=0
troisDouzTot=0
plusDouzTot=0

for x in listAge:
    if int(x) <3:
        moinsTrois=moinsTrois+1
    elif (int(x)>3 and int(x)<12):
        troisDouz=troisDouz+1
    elif (int(x)>12):
        plusDouz=plusDouz+1

moinsTroisTot=0*moinsTrois
troisDouzTot=10*troisDouz
plusDouzTot=15*plusDouz

tot=moinsTroisTot+troisDouzTot+plusDouzTot

print("Le prix total de tous les tickets de la famille est : ",tot)

names=["Marc", "Jean", "Mohamed"]

for n in names:
    print("Bonjour ", n , " Quel est votre age ? :")
    ageAdo = int(input())
    if ageAdo< 22:
        names.remove(n)

print("Liste des adolescents retenus pour rentrer sont : ", names)
