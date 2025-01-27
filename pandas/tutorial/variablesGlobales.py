x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print('-----------------------------------------------------')

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print('-----------------------------------------------------')

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print('-----------------------------------------------------')

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)