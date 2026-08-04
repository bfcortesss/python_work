# Tests for equality and inequality with strings
car = 'tesla'
car2 = 'tesla'
car3 = 'ford'

# Prints True
if (car == 'tesla' and (car2 == 'tesla')):
    print(car == 'tesla')
else:
    print(car != 'tesla')

# Prints False
if car == 'tesla' and car3 == 'tesla':
    print(car == 'tesla')
else:
    print(car != 'tesla')

# Tests using the lower() method --> Prints True
fruit = 'APPLE'

print(fruit.lower() == 'apple')

# Numerical tests involving equality and inequality
age_0 = 22
age_1 = 22

if (age_0 >= 21 and (age_1 >= 21)):
    print("Both are 21 or older")

if age_0 >= 21 or age_1 >= 21:
    print("At least one is 21 or older")

