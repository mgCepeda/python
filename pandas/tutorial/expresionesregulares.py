import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

print('-----------------------------------------------------')

# La findall()función devuelve una lista que contiene todas las coincidencias.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Devuelve una lista vacía si no se encontró ninguna coincidencia:
x = re.findall("Portugal", txt)
print(x)

print('-----------------------------------------------------')

# La search()función busca una coincidencia en la cadena y devuelve un objeto Match si hay una coincidencia.
# Si hay más de una coincidencia, solo se devolverá la primera aparición de la coincidencia:

# Busque el primer carácter de espacio en blanco en la cadena:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# Si no se encuentran coincidencias, devuelve el valor None:
# Realizar una búsqueda que no devuelva ninguna coincidencia:

x = re.search("Portugal", txt)
print(x)

print('-----------------------------------------------------')

# La split()función devuelve una lista donde la cadena se ha dividido en cada coincidencia:
# Dividir en cada carácter de espacio en blanco:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Dividir la cadena sólo en la primera aparición:
x = re.split("\s", txt, 1)
print(x)

print('-----------------------------------------------------')

# La sub()función reemplaza las coincidencias con el texto de su elección:
# Reemplace cada carácter de espacio en blanco con el número 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Reemplace las 2 primeras ocurrencias:
x = re.sub("\s", "9", txt, 2)
print(x)

print('-----------------------------------------------------')
# Realice una búsqueda que devolverá un objeto coincidente:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

print('-----------------------------------------------------')
# El objeto Match tiene propiedades y métodos que se utilizan para recuperar información sobre la búsqueda y el resultado:
# .span()devuelve una tupla que contiene las posiciones de inicio y fin de la coincidencia.
# .string devuelve la cadena pasada a la función.
# .group()devuelve la parte de la cadena donde hubo una coincidencia.
# Imprima la posición (posición inicial y final) de la primera coincidencia.
# La expresión regular busca cualquier palabra que comience con una "S" mayúscula:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())