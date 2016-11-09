# Creating a variable x with a formatter with value 10
x = "There are %d types of people." % 10
# Creating a variable binary and assign a string
binary = "binary"
# Creating a variable do_not and assign a string
do_not = "don't"
# Creating a variable y that prints a statement that includes binary and do_not variables as formatters
y = "Those who know %s and those who %s." %(binary, do_not)

# print the statement x
print x
# print the statement y
print y
# print statement with formatter %r taking in value from variable x
print "I said: %r." % x
# print statement with formatter %s taking in value from variable y
print "I also said: '%s'." % y

# Creating a boolean variable hilarious
hilarious = False
# Creating a statement joke_evaluation with a statement that takes formatter %r
joke_evaluation = "Isn't that joke so funny?! %r"
# print statement joke_evaluation
print joke_evaluation % hilarious

# Creating a variable w with a string value
w = "This is the left side of..."

# Creating a variable e with a string value
e = "a string with a right side."

# Concatenates variables w and e and prints them 
print w + e
