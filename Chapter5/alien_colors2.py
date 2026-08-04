# Choose a color for an alien. 
# 1. Write and if else chain
# if green print 5 points earned, if it is not green print that
# the player has earned 10 points.

# Write a version that passes the if block and another that passes 
# the else block.

alien_color = 'green'

if 'green' in alien_color:
    print("You have earned 5 points!")
else:
    print("You have now earned 10 points!")
# if block will be executed. 

alien_color = 'yellow'

if 'green' in alien_color:
    print("You have earned 5 points!")
else:
    print("\nYou have now earned 10 points!")
# else block will be executed

# If the color were set to red, then the else block will also execute.
alien_color = 'red'

if 'green' in alien_color:
    print("You have earned 5 points!")
else:
    print("\nYou have now earned 10 points!")