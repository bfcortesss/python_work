# lists 
# Created a list of bicycles
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Accessing elements in the list with the given indecies
#print(bicycles[0])
#print(bicycles[1])
#print(bicycles[2])
#print(bicycles[3])

# Print in consecutive order
#print(bicycles[0].title(),bicycles[1].title(), bicycles[2].title(), bicycles[3].title())

#print(bicycles[0].upper(),bicycles[1].upper(), bicycles[2].upper(), bicycles[3].upper())

# reutrns the last element in the list
#print(bicycles[-1].title())

# Accessing elements in the list with the given indecies using f-string
message = f"My first bicycle was a {bicycles[0].title()}."
#print(message)


# Modifying, adding, and removing elements in a list

# modifying an element in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

# adding an element to the end of the list
motorcycles.append('ducati')
#print(motorcycles)

# add an element to an empty list
cars = []
cars.append('tesla')
cars.append('ford')
cars.append('chevy')

#print(cars)

# adding an element to a specific position in the list using insert() method
cars.insert(0, 'honda')
#print(cars)

# removing an element from the list using del statement
del cars[0]
#print(cars)

# removing an element from the list using pop() method, and accessing the popped element
popped_cars = cars.pop()
#print(cars)
#print(popped_cars)

last_owned = motorcycles.pop()
#print(f"The last motorcycle I owned was a {last_owned.title()}.")

#print(motorcycles)

# Popping an items from any position in the list
#first_owned = motorcycles.pop(0)
#print(f"The first motorcycle I owned was a {first_owned.title()}.") 

#print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")

print(motorcycles)
