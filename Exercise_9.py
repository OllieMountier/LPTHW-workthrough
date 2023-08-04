# Exercise 9 is a continuation of printing. It teaches about formats such as creating new lines within strings, or using triple quotes to print as many lines as you wish.

# I had learnt about this, but haven't found much use for it inside my previous projects so sort of forgot it was available. After completing this book, I am keen to go through my old projects to see if I can neaten up my code using this lesson.

# There are no drills for this exercise, it just states to focus on what mistakes I have made and to try not to do make them again.

# setting variables ready to be used in the printing 
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

# testing the variables
print("Here are the days: ", days)
print("Here are the months: ", months)

# using three double quotes to allow the print function to print as many lines as it wants
print("""
      There's something going on here.
      With the three double quotes.
      We'll be able to type as much as we like.
      Even 4 lines if we want, or 5, or 6
      """)
