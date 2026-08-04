# imagine an alien was just shot down in a game.

# 1. Create a cariable called alien_color and assign a value 
# of either green, yellow, or red

# 2. Write an if statement to test whether the aliens color is green.
# print a message that the player has earned 5 point. 

alien_color = 'green'

if 'green' in alien_color:
    print("Alien Shot! You have earned 5 points.")

# 3. Write a test that fails. The result should be no output

alien_color = 'yellow'

if 'green' in alien_color:
    print("Alien Shot! You have earned 5 points.")

# This will produce no output. The first test passes so the output is 
# still produced for that. 

