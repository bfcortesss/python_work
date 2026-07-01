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

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
print(friend_foods)

print("\nMy friend's favorite foods are:")
print(my_foods)

