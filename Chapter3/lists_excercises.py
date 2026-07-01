# Chapter 3 - Lists Exercises
# 3-1 Names: Store names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.
names =  ['wendy','john', 'brisa', 'tony', 'mia']

#print(names[0].title())  # prints 'wendy'
#print(names[1].title())  # prints 'john'
#print(names[2].title())  # prints 'brisa'
#print(names[3].title())  # prints 'tony'
#print(names[4].title())  # prints 'mia'


# 3-2 Greetings: Start with the list you used in Exercise 3-1, 
# but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, 
# but each message should be personalized with the person’s name.
print(f"My friend {names[0].title()}, has some nice melons.")

print(f"{names[1].title()} is a great friend of mine.")

print(f"{names[2].title()} is very funny.")

print(f"{names[3].title()} is very generous.")

print(f"{names[4].title()} is very smart.")

# 3-3 Your Own List: Think of your favorite mode of transportation, 
# such as a motorcycle or a car, and make a list that stores several examples. 
# use your list to print a series of statements about these items,
cars = ['tesla', 'ford' , 'chevy', 'honda', 'toyota']

print(f"I woulds like to own a {cars[0].title()} by the end of 2027." "")

print(f"I would consider buying a {cars[1].title()} later in the future.")

print(f"If not then I would defintely consider buying a {cars[2].title()} truck.")

print(f"Even so, {cars[3].title()} have always been reliable.")

print(f"Im not really sure if I would get a {cars[4].title()}.")