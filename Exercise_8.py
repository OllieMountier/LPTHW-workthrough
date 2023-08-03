# This exercise focuses on more printing, especially using formatters. It demonstrates one of the uses of using the formatters.  

#It is more a demonstration rather than a drill and the drills are just checking work and understanding the use of quotations

# first we assign a formatter that can return any four variables
formatter = "%r %r %r %r"

#we use multiple print statements to demonstrate the use
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % ( "I had this thing,",
                   "That you could type upright,",
                   "but it didn't sing,",
                   "so I said goodnight"))