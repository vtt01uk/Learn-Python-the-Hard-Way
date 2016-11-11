# Import the sys module
from sys import argv
# Designates filename as the argument variable
script, filename = argv
# Uses the open method on filename and assigns it to variable txt
txt = open(filename)
# Prints statement that uses %r formatter that takes the filename variable
print "Here's your file %r:" % filename
# Uses read method on the txt variable
print txt.read()

# Prints statement
print "Type the filename again:"
# Assign user input as variable file_again
file_again = raw_input(">")
# Use the open method on variable file_again and assign it to txt_again
txt_again = open(file_again)
# Use the read method on the txt_again variable
print txt_again.read()
