# Testing multiple statements
requested_toppings = ['mushrooms' , 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperooni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# all of these tests are checked when we dont use an elif block or else block. 
# if we used an if-elif-else block, this would not work properly because 
# the code would stop running after only one test passes.
# This method can be used when we need multiple tests to pass.
