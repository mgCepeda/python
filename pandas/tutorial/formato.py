
# Crear una cadena f:
txt = f"The price is 49 dollars"
print(txt)

print('-----------------------------------------------------')

# Añade un marcador de posición para la price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

print('-----------------------------------------------------')
# Mostrar el precio con 2 decimales:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


print('-----------------------------------------------------')
# Mostrar el valor 95con 2 decimales:
txt = f"The price is {95:.2f} dollars"
print(txt)

print('-----------------------------------------------------')
# Realizar una operación matemática en el marcador de posición y devolver el resultado:
txt = f"The price is {20 * 59} dollars"
print(txt)

print('-----------------------------------------------------')
# Añadir impuestos antes de mostrar el precio:
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

print('-----------------------------------------------------')
# Devuelve "Caro" si el precio es superior a 50, de lo contrario devuelve "Barato":
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

print('-----------------------------------------------------')
# Utilice el método de cadena upper()para convertir un valor en letras mayúsculas:
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

print('-----------------------------------------------------')
# Crea una función que convierta pies en metros:
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

print('-----------------------------------------------------')
# Utilice una coma como separador de miles:
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

print('-----------------------------------------------------')
# Añade un marcador de posición donde quieras mostrar el precio:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

print('-----------------------------------------------------')
# Formatee el precio para que se muestre como un número con dos decimales:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

print('-----------------------------------------------------')
# Y agrega más marcadores de posición:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print('-----------------------------------------------------')
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print('-----------------------------------------------------')
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

print('-----------------------------------------------------')
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))