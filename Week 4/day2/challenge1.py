numb=int(input("Entrez un nombre : "))
leng=int(input("Entrez une longueur : "))

listMul=[]

mult=0
i=0

for i in range(1,leng+1) :
    listMul.append(numb*i)
print(listMul)