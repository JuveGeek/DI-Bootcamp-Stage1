users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
numbers = []

recreate_users_A_having_i=[]

for i in range(1, len(users)):
    numbers.append(i)

disney_users_A= dict(zip(users,numbers))
disney_users_B= dict(zip(numbers,users))


print(disney_users_A)

print("\n")

print(disney_users_B)

print("\n")

for a in range(0, int(len(users))):
    if "i" in users[a]:
        recreate_users_A_having_i.append(users[a])

users.sort()
disney_users_C= dict(zip(users,numbers))
print(disney_users_C)

print('i donne : ', recreate_users_A_having_i)