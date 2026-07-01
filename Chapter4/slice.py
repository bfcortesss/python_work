# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:4])
print(players[-3:])

# Slicing a list in a for loop
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# We have a list of favorite foods, 
# and we want to make a copy of that list for a friend.
my_foods = ['pizza', 'falafel', 'carrot cake'] # Remember to use brackets not curly braces when creating a list.
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
print(friend_foods)

print("\nMy friend's favorite foods are:")
print(my_foods)

# OUTPUT: Should contain the same list of foods for both statements.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# This proves that we are working with two seperate lists. 

# This approach will not work. 
# you cants copy a list without using slice.
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# In this case setting friend_foods equal to my_foods does not create a copy of the list. 
# Instead, it creates a reference to the original list. 
# As a result, any changes made to my_foods will also affect friend_foods, and vice versa.
