# This exercise is used to first introduce the student to names and variables. Here the variables
# will be assigned values and used in calculations rather than just using the values themselves.

# The drills include of recorrecting floating point isses- which doesn't affect me, writing comments
# to get into the habit and also answering a couple rudimentary questions.

# This section is the assignment of values to variable names relating to carpool cars and passengers
cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

# Now we will return these values inside strings back to the user
print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, " people today")
print("We have", passengers, "passengers to carpool today")
print("we need to put about", average_passengers_per_car, "passengers in each car")


