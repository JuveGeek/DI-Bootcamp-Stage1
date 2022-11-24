my_fav_numbers=set()

#Add two new numbers to the set
my_fav_numbers.add(12)
my_fav_numbers.add(23)

#Remove the last number.
my_fav_numbers.remove(12)


#Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers=set()

friend_fav_numbers.add(13)
friend_fav_numbers.add(32)
friend_fav_numbers.add(4)

#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)


print(our_fav_numbers)