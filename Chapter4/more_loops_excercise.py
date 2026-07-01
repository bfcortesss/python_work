# 1. More loops: Choose a version of foods.py,
# and write two for loops to print each list of foods.

foods = ['burgers' , 'steak' , 'pasta' , 'chicken']
desserts = ['ice cream' , 'cake' , 'cheesecake' , 'pudding']

print("My favorite dinner time foods are:")
for food in foods[:]:
    print(food.title())

print("\nMy favorite sweet treats are:")
for dessert in desserts[:]:
    print(dessert.title())
