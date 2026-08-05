"""
Write an if-elif-else chain that determines a persons stage of life.

1. Set a value for the variable age.

2. If a person is less than two years old print a message that the
person is a baby.

3. If a person is at least 2 years old but less than 4, print toddler.

4. If a person is at least 4 years old but less than 13, print kid. 

5. If a person is at least 13 years old but less than 20, print teenager. 

6. If a person is at least 20 years old but less than 65, print adult. 

7. If a person is age 65 or older, print elder. 

"""

age = 1

if age < 2:
    print("Baby")
elif age >= 2 and age <= 4:
    print("Toddler")
elif age >= 4 and age <= 13:
    print("Kid")
elif age >= 13 and age <= 20:
    print("Teenager")
elif age >= 20 and age <= 65:
    print("Adult")
else:
    print("Elder")
# OUTPUT: Baby

age = 2

if age < 2:
    print("Baby")
elif age >= 2 and age <= 4:
    print("\nToddler")
elif age >= 4 and age <= 13:
    print("Kid")
elif age >= 13 and age <= 20:
    print("Teenager")
elif age >= 20 and age <= 65:
    print("Adult")
else:
    print("Elder")
# OUTPUT: Toddler

age = 6

if age < 2:
    print("Baby")
elif age >= 2 and age <= 4:
    print("Toddler")
elif age >= 4 and age <= 13:
    print("\nKid")
elif age >= 13 and age <= 20:
    print("Teenager")
elif age >= 20 and age <= 65:
    print("Adult")
else:
    print("Elder")
# OUTPUT: Kid

age = 14

if age < 2:
    print("Baby")
elif age >= 2 and age <= 4:
    print("Toddler")
elif age >= 4 and age <= 13:
    print("Kid")
elif age >= 13 and age <= 20:
    print("\nTeenager")
elif age >= 20 and age <= 65:
    print("Adult")
else:
    print("Elder")
# OUTPUT: Teenager

age = 21

if age < 2:
    print("Baby")
elif age >= 2 and age <= 4:
    print("Toddler")
elif age >= 4 and age <= 13:
    print("Kid")
elif age >= 13 and age <= 20:
    print("Teenager")
elif age >= 20 and age <= 65:
    print("\nAdult")
else:
    print("Elder")
# OUTPUT: Adult

age = 66

if age < 2:
    print("Baby")
elif age >= 2 and age <= 4:
    print("Toddler")
elif age >= 4 and age <= 13:
    print("Kid")
elif age >= 13 and age <= 20:
    print("Teenager")
elif age >= 20 and age <= 65:
    print("Adult")
else:
    print("\nElder")
# OUTPUT: Elder