# Exercise 10 teaches about input. The book is based off of Python 2 so uses raw_input rather than input. The basic code also looks as though it could be improved as it sets the variable to the input from the print statement rather than taking the value directly from the input. Whether this is the format for raw_input I am not sure as I never used this in my code.

# The drills just go over the input, which I have already completed in my education. My most current work using the input function is to automate a modelling file, whether it runs on my learning code, or a full code containing multiple ML models and a Neural Network. It requires many inputs from the user but in the end will hopefully present to future employers and colleagues the capacity of my experience rather than just following lessons and exercises.

# We are tasked to get 3 variables from the user
age = int(input("What is your age? "))
height = int(input("How tall are you? "))
weight = float(input("How much do you weigh? "))

# We then return the variables back in a sentence containing their details
print("So you're %r years old, %rcm tall and you weigh %rkg" % (age, height, weight))

# I have edited the code to transform the variables to the integer/float data type as it makes the return look cleaner