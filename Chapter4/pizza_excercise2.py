# 1. Make a copy of the list pizzas and call it friend_pizza.
# 2. Add a new pizza to the original list.
# 3. Add a different pizza to the list of friend_pizzas
# 4. Prove that you have two seperate lists.
#   - print a message that displays each seperate list, using a for loop.

pizzas = ['pepperoni' , 'hawaiin' , 'meat lovers']

friend_pizzas = pizzas[:]

print("My favorite pizzas are:")
for pizza in pizzas[:]:
    print(pizza)

print("\nMy friends favorite pizzas are:")
for pie in friend_pizzas[:]:
    print(pie)

