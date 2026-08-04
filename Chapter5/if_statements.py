# The simplest kind of if statement is the one that checks a condition 
# and executes a block of action.

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
# Since the conditional test passed. Both print calls are executed

# if-else
age = 17

if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18.")

# Whichever conditional test passes determines which code block gets executed.

# The if-elif-else Chain

age = 12
if age < 4:
    print("\nYour admission is FREE!")
elif age < 18:
    print("\nyour admission is $25.")
else:
    print("\nyour admissions is $40.")

# In this case the elif code block is what is executed. 

# Another way to organize and if-elif-else statement using the example above.
age = 1

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"\nyour admission cost is ${price}.")

# Using multiple elif blocks
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"\nYour admission cost is ${price}")

# In this case the second elif block checks to make sure a person is less 
# than the age of 65 before assigning the full admission rate
# The else blocks price is set to $20 because only the individuals 
# that are older than 65 receive an admission cost of $20

# Omitting the else block
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"\nYour admission cost is ${price}")

#Sometimes, an else block is useful. Other times, 
# it’s clearer to use an additional elif statement that catches the 
# specific condition of interest