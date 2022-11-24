fruits=input("Quels sont vos fruits préférés ? (Séparez chaque fruit par un seul espace) ")

list_fruits=fruits.split()

x= input("Entrez le nom d'un fruit")

if x in list_fruits:
    print("Tu as choisit un de tes fruits préférés ! profites")
else:
    print("Tu as choisit un nouveau fruit")