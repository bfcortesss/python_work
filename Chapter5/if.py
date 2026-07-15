# An example of an if statement in a for loop
cars = ['audi' , 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Check for inequality 
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

# Check multiple conditions using and
age_0 = 22
age_1 = 22

if (age_0 >= 21 and (age_1 >= 21)):
    print("Both are 21 or older")

age_0 = 18

age_0 >= 21 or age_1 >= 21
print("At least one is 21 or older")

# Check whether a value is in a list
requested_toppings = ['mushrooms' , 'onions' , 'pineapple']
'mushrooms' in requested_toppings

print("\ntrue")

