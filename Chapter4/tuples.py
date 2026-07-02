# Tuples are considered immutable lists. In other words,
# it is a list that contains values that cannot be changed.
dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# OUTPUT: Should display 200 and 50 respectively

dimensions[0] = 250

# This will produce an error: 'tuple' object does not support assignmnet.


# Looping through a Tuple
for dimension in dimensions:
    print(dimension)

# OUTPUT: This will return the tuples values.

# We can write over a tuple and assign new values to the variable.
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
