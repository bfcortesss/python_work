""" 
Make a list of your favorite fruits, write a series of independent if statements that
checks certain fruits in the list. 

1. Create a list of your three fave foods and call it favorite_fruits.

2. Write five if statements. Check if a certain fruit is in the list and print a statement
for the certain code block. 
"""

favorite_fruits = ['bananas' , 'mangos' , 'apples']

if 'bananas' in favorite_fruits:
    print(f"I like {favorite_fruits[0].title()}")
if 'mangos' in favorite_fruits:
    print(f"\nI also really like {favorite_fruits[1].title()}")
if 'apples' in favorite_fruits:
    print(f"\nI like {favorite_fruits[2].title()} too.")

print("\nHowever, I don't like Grapes.")

