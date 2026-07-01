""" 
Python Crash Course 3-10 Every Function: 

Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, 
cities, languages, or anything else you’d like. 

Write a program that creates a list containing these items and 
then uses each function introduced in this chapter at least once. 
"""

cities = ['denver' , 'los angeles' , 'aurora' , 'san diego']

#print(cities)

# print from a specified index 
# print(cities[0].title())
# print(cities[1].title())
# print(cities[-1].title())

# use values from a list
message = f"I currently reside in {cities[2].title()}, Colorado."
#print(message)

# modifying elements in list
cities[0] = 'colorado springs'
#print(cities)

# adding to a list using append
cities.append('denver') # will add to the end of the list
#print(cities)

# adding to a list using insert 
cities.insert(0, 'san francisco') # Allows us to insert at a given index 
##print(cities)

# removing from a list using del 
del cities[0] # will remove San Francisco
#print(cities)

# removing from a list using pop() method
popped_city = cities.pop() # Will pop from the top of the stack
#print(cities)

#print(f"The city that was removed is: {popped_city.title()}")

# you can pop from any given index
cities.pop(0)
#print(cities)

# removing by a given name/value
cities.remove('aurora')
#print(cities)

# add removed new cities you would live in
cities.append('seattle')
cities.append('chicago')
#print(f"The cities that I would love to live in: {'san diego'.title()}, and {'chicago'.title()}.")

print(cities)

# use sorted() method
print(sorted(cities))

# show that the list is still in its orginal order
print(cities)

# use reverse to change the order of your list
cities.reverse()
print(cities)

# change the list back to it's original order
cities.reverse()
print(cities)

# use sort()
cities.sort()
print(cities)

# use sort to put the list in reverse-alphabetical order
cities.sort(reverse=True)
print(cities)

# use len to display the total number of desired destinations
print(len(cities))
