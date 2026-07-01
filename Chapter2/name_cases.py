# python crash course Chapter 2 Excercise 2-4
# name cases:  Use a variable to represent a person’s name, and then
# print that person’s name in lowercase, uppercase, and title case.

persons_name = "brian flores"
message = f"{persons_name}"

#print(message.lower())
#print(message.upper())
#print(message.title())


# Excercise 2-5 
# Famous quote:  Find a quote from a famous person you admire. Print
# the quote and the name of its author. Your output should look something like

author = "Albert Einsteen"
quote_message = "once said, A person who never made a mistake never tried anything new."

message2 = f"{author} {quote_message}"

#print(message2)

# Excercise 2-6 
# Famous Quote 2: satisfied with previous excercise.


# Excercise 2-7
# Stripping Names: Store a person’s name, and include some whitespace
# at the beginning and end of the name. Make sure you use each character-
# istic function, lstrip(), rstrip(), and strip() to remove the whitespace.


message_with_identation = "     Fruits:\n\tApple.   \n\t. Banana.  \n\tChe  rry"

#print(message_with_identation)

name_with_whitespace = "   Brian Flores   "

#print(name_with_whitespace)
#print(name_with_whitespace.lstrip())
#print(name_with_whitespace.rstrip())
#print(name_with_whitespace.strip())

#Excercise 2-8
# Python has a removesuffix() method that removes a suffix from a string. 
# If the string doesn’t end with the specified suffix, the original string is returned. 
# Use removesuffix() to remove the suffix “.txt” from a filename.

filename = "HTTPS://www.document.txt"

print(filename.removeprefix("HTTPS://www.").removesuffix(".txt"))
