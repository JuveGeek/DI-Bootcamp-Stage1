family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

nbMoinsTrois=0
nbMoinssDouz=0
nbPlusDouz=0

for key,val in family.items():
    if val < 4:
        print(key, "doit payer 0 $ ")
    elif val < 13:
        print(key, "doit payer 10 $ ")
        nbMoinssDouz=nbMoinssDouz+1
    else: 
        print(key, "doit payer 15 $ ")
        nbPlusDouz=nbPlusDouz+1

print("Prix total es égal à : ",nbMoinssDouz*10+nbPlusDouz*15)