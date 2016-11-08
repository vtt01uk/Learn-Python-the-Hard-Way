# Creating a variable called car with a value of 100
cars = 100
# Creating a variable called space_in_a_car that has a floating point value of 4.0
space_in_a_car = 4.0
# Creating a variable called drivers with a value of 30
drivers = 30
# Creating a variable called passengers with a value of 90
passengers = 90
# Creating a variable called cars_not_driven that deducts the value of variable drivers from the variable value of cars
cars_not_driven = cars  - drivers
# Creating a variable called cars_driven that is equal in value to drivers variable
cars_driven = drivers
# Creating a variable called carpool_capacity that multiplies cars_driven and space_in_a_car together
carpool_capacity = cars_driven * space_in_a_car
# Creating a variable called average_passengers_per_car that divides passengers by cars_driven
average_passengers_per_car = passengers / cars_driven


# Concatenates print statement with variable values
print "There are", cars, "cars available."
# Concatenates print statement with variable values
print "There are only", drivers, "drivers available."
# Concatenates print statement with variable values
print "There will be", cars_not_driven, "empty cars today."
# Concatenates print statement with variable values
print "We can transport", carpool_capacity, "people today."
# Concatenates print statement with variable values
print "We have", passengers, "to carpool today."
# Concatenates print statement with variable values
print "We need to put about", average_passengers_per_car, "in each car."
