# Exercise 4 from learning python the hard way: Variables and Names
# The following lines are from the exercise

cars = 100 # number of cars
space_in_a_car = 4.0 # space in the car
drivers = 30 # number of drivers
passengers = 90 # number of passangers 
cars_not_driven = cars - drivers #Using code from lines  4 and 6 to create a mathmatical express that revels how many cars aren't driven..
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers /cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


