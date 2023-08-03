## This exercises teaches about variables and printing. It uses format strings to return embedded print statements

## I never really learnt about format strings, which now gives extra reasoning to go over this book- to revise content
## i already know, and also to learn the fundamental's of Python I may have originally missed.

# The drills for this exercise focus on understanding and learning format strings. It gets you to research the format 
# strings and alter the below code. It also continues to make the student to use comments to describe code.

# I have changed the variables in the book from the authors personal details, to my own.
my_name = 'Ollie Mountier'
my_age = 20
my_height = 178 #inches
my_weight = 104.1 #kilograms
my_eyes = "Blue"
my_teeth = "white"
my_hair = "blond"

# printing the variables embedded in strings is something I need to get used to. Its proven complicated to transfer over to this version but I will now focus on using this in future exercises
print("Lets talk about %s." %my_name)
print("He's %d inches tall" % my_height)
print("He's %d kilograms heavy" % my_weight)
print("Thats actually not too heavy")
print("He's got %s eyes and %s hair" % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee" % my_teeth)

# To challenge the student, he included a sum using the format strings. However, with practice in difficult sums already
# it was just nice to further practice the format repetitively
print("If i add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight))
