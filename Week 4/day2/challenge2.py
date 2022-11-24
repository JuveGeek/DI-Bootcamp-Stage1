ss= input("Entrer une chaine de caractères : ")
new_s = ""
prev = ""
for c in ss:
    if len(new_s) == 0:
        new_s += c
        prev = c
    if c == prev:
        continue
    else:
        new_s += c
        prev = c
 

print("La nouvelle chaine est : ",new_s)