# Declare a function that takes cheese_count and boxes_of_crackers as parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# Print statement that takes % cheese_count formatter
  print "You have %d cheeses!" % cheese_count
# Print statement that takes % boxes_of_crackers formatter
  print "You have %d boxes of crackers!" % boxes_of_crackers
# Print statement
  print "Man that's enough for a party!"
# Print statement followed by a new line
  print "Get a blanket.\n"

# Print statement
print "We can just give the function numbers directly:"
# Calls functions and assigns values to parameters
cheese_and_crackers(20, 30)
# Print statement
print "OR, we can use variables from our script:"
# Assign value to new variable
amount_of_cheese = 10
# Assign value to new variable
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

