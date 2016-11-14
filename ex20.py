# Import arguments from sys module
from sys import argv
# Assign input_file as argv
script, input_file = argv

# Define a function that takes f as parameter
def print_all(f):
# Reads f parameter and prints it
  print f.read()

# Define a function that takes f as parameter
def rewind(f):
# Call seek method on f parameter starting at the first byte
  f.seek(0)

# Define a function with line_count and f parameters
def print_a_line(line_count, f):
# Prints value of line_count variables and runs readline method on f parameter
  print line_count, f.readline()

# Calls open method on argument (input_file) and assign it to current_file
current_file = open(input_file)

# Print statement
print "First let's print the whole file:\n"

# Calls function using current_file variable
print_all(current_file)

# Print statement
print "Now let's rewind, kind of a tape."

# Calls function using current_file variable
rewind(current_file)

# Print statement
print "Let's print three lines:"

# Defining variable with value of 1
current_line = 1
# Call function using current_line and current_file as parameters
print_a_line(current_line, current_file)

# Incrementing value of current_line
current_line = current_line + 1
# Call function using current_line and current_file as parameters
print_a_line(current_line, current_file)

# Incrementing value of current_line
current_line = current_line + 1
# Call function using current_line and current_file as parameters
print_a_line(current_line, current_file)
