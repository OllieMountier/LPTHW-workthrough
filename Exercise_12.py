#   Exercise 12 expands on the input function. The way the book had written their code is apparently the basic form which I never learnt. This exercise teaches the "advanced" way which is assigning the variable directly to the input function. As I have already completed this assignment, I will demonstrate the "basic" from below that I was originally meant to do in the previous exercise.

# The study drills for this teach about using pydoc. I have never heard of this but have read it is useful for open source coding and sharing code.

# We get the same variables as previous, but using a different, longer format
print("How old are you? "),
age = float(input())
print("How tall are you? "),
height = float(input())
print("How much do you weigh? "),
weight = float(input())

# We then return the variables back with the users personal details
print("So you're %r years old, %rcm tall and %rkg" % (age, height, weight))

