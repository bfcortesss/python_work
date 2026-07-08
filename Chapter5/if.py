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