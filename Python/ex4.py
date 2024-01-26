#Now you can things with print and you can do math. 
#The next step is to learn about variables.
#In programing, a variable is nothing more than a name for something, 
#similar to how my name "Zed", is a name for "human who wrote this book."
#Programmers use these varibale names to nake their code read more like English and because they have lousy memories.
#If they don't use good name for things in their sofeware, they'dget lost when they tired to reas their code again.


cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_drivern = drivers
carpool_capacity = cars_drivern * space_in_car
average_passengers_per_car = passengers / cars_drivern

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")