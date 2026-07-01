# Using the range() function

#for value in range(1, 6):
    #print(value)

numbers = list(range(1, 6))
#print(numbers)

even_numbers = list(range(2, 11, 2))
#print(even_numbers)

squares = [] # Creating an empty list 
for value in range(1, 11):
    squares.append(value**2)

print(squares)
