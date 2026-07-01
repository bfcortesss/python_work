# Python Crash Course - Chapter 2: Variables and Simple Data Types

firstname = "ada"
lastname = "jones"
fullname = f" {firstname} {lastname}"

# Stored the message in a variable called "message"
message = f"Hello, {fullname.title()}"
#print(message)

# Demonstrating string methods
# print(message.title())
# print(message.upper())
# print(message.lower())

# Stripping whitespace
favorite_language = " python "
#print(favorite_language)
#print(favorite_language.rstrip())
#print(favorite_language.lstrip())
#print(favorite_language.strip())

# Removing prefixes
nostarch_url = "https://nostarch.com"
simpleurl = nostarch_url.removeprefix("https://")
print(simpleurl)  # Output: nostarch.com