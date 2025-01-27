# Convertir de JSON a Python:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

print('-----------------------------------------------------')

# Convertir de Python a JSON:
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

print('-----------------------------------------------------')
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print('-----------------------------------------------------')
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# El ejemplo anterior imprime una cadena JSON, pero no es muy fácil de leer, sin sangrías ni saltos de línea.
# El json.dumps()método tiene parámetros para facilitar la lectura del resultado:
# Utilice el indentparámetro para definir el número de sangrías:
print('-----------------------------------------------------')
print(json.dumps(x, indent=3))

print('-----------------------------------------------------')
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print('-----------------------------------------------------')
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
