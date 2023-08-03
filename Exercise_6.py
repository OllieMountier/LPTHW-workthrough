# This exercise teaches the use of variables inside strings in more detail. It further goes through the use of format characters and also abbreviating variable names.

# The drills at the end are just going over the code below and making sure the student understands it well- the code and also the more indepth answers like why combining strings makes it longer. It further touches on commenting but I hope in later exercises it phases this out as it becomes muscle memory for the student.

#This runs through format characters and strings based on binary
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" %(binary, do_not)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s'." %y)

#This section assigns boolean value to a variable ready to be printed in a Q&A style statement
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print(joke_evaluation % hilarious)

#Now we are learning to combine strings and add them together
w = "This is the left side of..."
e = "a string with a right side"

print(w + e)