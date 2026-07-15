"""  
Chapter 5-1 Condtional Tests. 
Write a series of conditional tests. Print a statement describing each test
and your prediction of the result. 

Create at least 10 tests. Have at least 5 evaluate to True, and 
5 tests evaluate to False.
"""

# 1st set of tests
car = 'tesla'

print("Is the car == 'tesla'? I predict yes.")
print(car == 'tesla')

print("\nIs car == 'audi'? I predict false.")
print(car == 'audi')

# 2nd set of tests 
age = 28

print("\nThe following result will be True.")
print(age == 28)

print("\nIs the age 18? This result will be false")
print(age == 18)

# 3rd set of tests 
toppings = ['ham' , 'pepperoni' , 'pineapple' , 'jalapanoes']

print("\nThis will be True.")
print('pepperoni' in toppings) 

print("\nThis will be False.")
print('onions' in toppings)

# 4th set of tests 
name = 'brian'

print("\nThe following will be True.")
print(name == 'brian')

print("\nThe following will be false.")
print(name != 'brian')

# 5th set of tests 
