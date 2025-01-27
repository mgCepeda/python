class MyClass:
  x = 5

print(MyClass)

print('-----------------------------------------------------')
p1 = MyClass()
print(p1.x)

print('-----------------------------------------------------')
# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


print('-----------------------------------------------------')
# The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


print('-----------------------------------------------------')
# The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

print('-----------------------------------------------------')
# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

print('-----------------------------------------------------')
# Set the age of p1 to 40:
p1.age = 40
print(p1.age)

print('-----------------------------------------------------')
# Delete the age property from the p1 object:
del p1.age
# print(p1.age)

# Delete the p1 object:
del p1
