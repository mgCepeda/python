cars = ["Ford", "Volvo", "BMW"]

print(cars)

# Get the value of the first array item:

x = cars[0]
print(x)

# Modify the value of the first array item:

cars[0] = "Toyota"
print(cars)

# Return the number of elements in the cars array:

x = len(cars)
print(x)


print('-----------------------------------------------------')
# Print each item in the cars array:
for x in cars:
  print(x)

print('-----------------------------------------------------')
# Add one more element to the cars array:
cars.append("Honda")
print(cars)

print('-----------------------------------------------------')
# Delete the second element of the cars array:
cars.pop(1)
print(cars)

print('-----------------------------------------------------')
# Delete the element that has the value "Volvo":
cars.remove("BMW")
print(cars)
