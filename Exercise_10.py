# Exercise 10 further teaches on the lesson in exercise 9. It explains the use for escape sequences and lists off all the available ones in Python.

# My experience with escape sequences is purely an understanding of what they do rather than practical use. I learnt about them when studying data cleaning as I was having issues with the backslash. To my knowledge, I haven't used any previously but again will be going over my code to see if I can add them in to make the code more presentable and efficient.

# The drills in this task are to study and memorise the escape sequences, and using these with format strings.

# first we set some basic variables to ease in to the exercise
tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat="I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)