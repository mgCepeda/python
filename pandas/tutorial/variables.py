x = 5
y = "John"
print(x)
print(y)

print('-----------------------------------------------------')

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

print('-----------------------------------------------------')

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

print('-----------------------------------------------------')

# Get the type
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

print('-----------------------------------------------------')

# Case-Sensitive
a = 4
A = "Sally"

#A will not overwrite a

print(a)
print(A)

# Cómo consultar el tipo de dato
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
print(type(print("Mi cadena de texto")))  # Tipo 'NoneType'

x = ["apple", "banana", "cherry"]	
#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')

x = ("apple", "banana", "cherry")
#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')
x = range(6)	
#display x:
print(x)

#display the data type of x:
print(type(x)) 	
print('-----------------------------------------------------')

x = {"name" : "John", "age" : 36}	

#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')

x = {"apple", "banana", "cherry"}	

#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')

x = frozenset({"apple", "banana", "cherry"})
#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')

x = b"Hello"
#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')

x = bytearray(5)	
#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')

x = memoryview(bytes(5))	
#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')

x = None
#display x:
print(x)

#display the data type of x:
print(type(x)) 

print('-----------------------------------------------------')

### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

print('-----------------------------------------------------')

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

print('-----------------------------------------------------')

my_bool_variable = False
print(my_bool_variable)

print('-----------------------------------------------------')

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

print('-----------------------------------------------------')

# Algunas funciones del sistema
print(len(my_string_variable))

print('-----------------------------------------------------')

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

x = y = z = "Orange"
print(x)
print(y)
print(z)

print('-----------------------------------------------------')

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print('-----------------------------------------------------')

# # Inputs
# name = input('¿Cuál es tu nombre? ')
# age = input('¿Cuántos años tienes? ')
# print(name)
# print(age)

print('-----------------------------------------------------')

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# print('-----------------------------------------------------')

# ¿Forzamos el tipo?
address: str = "Mi dirección"
print(type(address))
address = True
print(type(address))
address = 5
print(type(address))
address = 1.2
print(type(address))
