brand={
    "name": "Zara", 
    "creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona" ,
    "type_of_clothes": "men, women, children, home" ,
    "international_competitors": ["Gap", "H&M", "Benetton"] ,
    "number_stores": 7000, 
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": "pink, green"
    }   
}

brand["number_stores"]=2

print("Zaras clients sont des hommes;femmes,enfants,...")

brand["country_creation"]="Spain"

if "international_competitors" in brand:
    print("Oui international_competitors est présent")
    brand["international_competitors"].append("Desigual")
else:
    print("Oui international_competitors n'est présent")

del brand["creation_date"]

lng=int(len(brand["international_competitors"]))

print("Dernier compétiteur international est : ",brand["international_competitors"][lng-1])

for cle,val in brand["major_color"].items():
    print("Major clothes clolor sont : ", val ,"pour", cle )

print("Longueur du dictionnaire est : ", len(brand))

print("Les différentes clefs su dictionnaire sont : \n")
for cle,val in brand.items():
    print(cle)

more_on_zara={
    "creation_date": 1975,
    "number_stores": 10000,
}

brand.update(more_on_zara)

print("number stores : ",brand["number_stores"])

