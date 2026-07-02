# 1. Think of five simple foods, and store them in a Tuple.
# 2. Use a for loop to print each food the returant offers.
# 3. Attempt to modify an item in the list to demonstarte an error.
# 4. Add a line that rewrites the Tuple, Use a for loop to display the revised menu.

food_options = ('fries' , 'onion rings' , 'mozarella sticks' , 'cheese curds' , 'fried pickles')

print("The resturant offers the following appetizers:")
for food in food_options:
    print(food.title())

#food_options[0] = 'nachos' # SUCCESS, produced intended error

food_options = ('fries' , 'nachos' , 'sliders' , 'wings' , 'fried pickles')

print("\nThe revised appetizer menu includes the following:")
for food in food_options:
    print(food.title())