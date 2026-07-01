# 1. Use a for loop to print the numbers 1 to 20.
for value in range(1, 21):
    print(value)

# 2. Make a list pf numbers from one to one milliom
#  - Use a for lop to print thr numbers
for nums in range(1, 10000001):
    print(nums)

# 3. Make a list of numbers from 1 to one million. 
# - use sum(), max(), and min() functions.
numbers = list(range(1, 10000001))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 4. make a list of odd numbers using the range function
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)

# 5. make a list of the multiples of 3, from 3 to 30.
threes = list(range(3, 31, 3))
for three in threes:
    print(three)

# 6. make a list of first 10 cubes, and use a for loop to print each one.
cubed = []
for value in range(1, 11):
    cubed.append(value**3)

print(cubed)

# 7. Use a list comprehesnion to generate a list of the first 10 cubes.
cubed = [value**2 for value in range(1, 11)]
print(cubed)