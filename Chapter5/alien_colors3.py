# Now turn the if-else chain previously used into 
# an if-elif-else chain

# 1. green = 5 points 
# 2. yellow = 10 points 
# 3. red = 15 points 
# write three versions where each test passes. 

alien_color = 'green'

if alien_color == 'green':
    print("You have earned 5 points!")
elif alien_color == 'yellow':
    print("You have earned 10 points!")
else:
    print("you have earned 15 points")
# first test will pass.

alien_color = 'yellow'

if alien_color == 'green':
    print("You have earned 5 points!")
elif alien_color == 'yellow':
    print("\nYou have earned 10 points!")
else:
    print("you have earned 15 points")
# second test will pass

alien_color = 'red'

if alien_color == 'green':
    print("You have earned 5 points!")
elif alien_color == 'yellow':
    print("You have earned 10 points!")
else:
    print("\nYou have earned 15 points")
# the third test will pass 

