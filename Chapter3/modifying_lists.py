# Chapter 3 Exercises 
# 3-4 Guset List: If you could invite anyone, living or deceased, to dinner, 
# who would you invite? make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.
guest_list = ['Albert Einsteen' , 'Barack Obama' , 'Satoru Gojo']

#print(f"Hello {guest_list[0].title()}, you're invited to dinner at Olive Garden.")

#print(f"Hello {guest_list[1].title()}, you're invited to pizza and drinks.")

#print(f"Hello {guest_list[2].title()}, you're invited to a carne asada at my house.")

#print(guest_list)

# 3-5 Changing Guest List: You just heard one of your guests can't make it. 
# You need to send a new inivitation. Think of someone else to invite.

# TODO: Remove guest from list and state the name of the guest that is unable to make it.
unable_to_attend = guest_list.pop(0)
#print(f"{unable_to_attend} is unable to attend.")

# TODO: Invite/add a new guest to the guest_list
guest_list.insert(0, 'Yuji Itadori')
#print(guest_list)

#TODO: Print invitation for the new guest
#print(f"{guest_list[0]}, you are now invited to dinner at Olive Garden.")

# TODO: Print the current guest list
#print(f"The current guests include: {guest_list[0]}, {guest_list[1]}, and {guest_list[2]}.")

# 3-5 More Guests

#print(f"Hello {guest_list[0]}, {guest_list[1]}, and {guest_list[2]}! a bigger table has been found for dinner.")

# TODO: use insert() to add one new guest to the beginning of the list. 
guest_list.insert(0, 'John Summit')
#print(guest_list)
# TODO: use insert() to add one new guest to the middle of the list.
guest_list.insert(2, 'Murph')
#print(guest_list)
# TODO: use append() to add one new guest to the end of your list. 
guest_list.append('Kaskade')
#print(guest_list)

#print(f"Hello {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, {guest_list[5]} you guys are all ivited to dinner.")


# 3-7 Shrinking guest list. 
#print(f"Hello {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, {guest_list[5]} the table only fits two people.")

univited = guest_list.pop(0), guest_list.pop(1), guest_list.pop(2), guest_list.pop()
#print(f"Hello {univited}, I am sorry but you cannot come to dinner.")

#print(guest_list)

#print(f"Hello {guest_list[0]}, you are still invited to dinner.")
#print(f"hello {guest_list[1]}, you are also still invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)

# 3-9 Total Dinner Guests
print(len(guest_list))