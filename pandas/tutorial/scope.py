# Una variable creada dentro de una función está disponible dentro de esa función:
def myfunc():
  x = 300
  print(x)

myfunc()

print('-----------------------------------------------------')

# Se puede acceder a la variable local desde una función dentro de la función:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

print('-----------------------------------------------------')

# Una variable creada fuera de una función es global y puede ser utilizada por cualquiera:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

print('-----------------------------------------------------')

# La función imprimirá el local x y luego el código imprimirá el global x:
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

print('-----------------------------------------------------')

# Si utiliza la globalpalabra clave, la variable pertenece al ámbito global:
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Para cambiar el valor de una variable global dentro de una función, haga referencia a la variable utilizando la globalpalabra clave:
x = 300

print('-----------------------------------------------------')

def myfunc():
  global x
  x = 200

myfunc()

print(x)

print('-----------------------------------------------------')

# Si utiliza la nonlocalpalabra clave, la variable pertenecerá a la función externa:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
