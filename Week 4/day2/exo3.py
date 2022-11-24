basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#Remove “Banana” from the list.
basket.remove("Banana")

#Remove “Blueberries” from the list.
basket.remove("Blueberries")

#Add “Kiwi” to the end of the list.
basket.append("Kiwi")

#Add “Apples” to the beginning of the list.
basket.append("Apples")

nb=0

#Count how many apples are in the basket.
for x in basket:
    if(x=="Apples"):
        nb=nb+1
print("\n nombre de Apples est =",nb)

#Empty the basket
basket.clear()

print(basket)
