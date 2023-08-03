## This exercises teaches about variables and printing. It uses format strings to return embedded print statements

## I never really learnt about format strings, which now gives extra reasoning to go over this book- to revise content
## i already know, and also to learn the fundamental's of Python I may have originally missed.

# The drills for this exercise focus on understanding and learning format strings. It gets you to research the format 
# strings and alter the below code. It also continues to make the student to use comments to describe code.

# I have changed the variables in the book from the authors personal details, to my own.
name = 'Ollie Mountier'
age = 20
height = 178 #inches
weight = 104.1 #kilograms
eyes = "Blue"
teeth = "white"
hair = "blond"

# printing the variables embedded in strings is something I need to get used to. Its proven complicated to transfer over to this version but I will now focus on using this in future exercises
print("Lets talk about %s." %name)
print("He's %d inches tall" % height)
print("He's %d kilograms heavy" % weight)
print("Thats actually not too heavy")
print("He's got %s eyes and %s hair" % (eyes, hair))
print("His teeth are usually %s depending on the coffee" % teeth)

# To challenge the student, he included a sum using the format strings. However, with practice in difficult sums already
# it was just nice to further practice the format repetitively
print("If i add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight))
