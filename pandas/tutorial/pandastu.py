import pandas as pd
print(pd.__version__)

# df = pd.read_csv('datos.csv')

# print(df.to_string()) 

print('-----------------------------------------------------')
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

print('-----------------------------------------------------')

# Crea una serie Pandas sencilla a partir de una lista:
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Si no se especifica nada más, los valores se etiquetan con su número de índice. El primer valor tiene índice 0, el segundo valor tiene índice 1, etc.
# Esta etiqueta se puede utilizar para acceder a un valor específico.
# Devuelve el primer valor de la serie:

print(myvar[0])


print('-----------------------------------------------------')
# Crea tus propias etiquetas:
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

# Devuelve el valor de "y":
print(myvar["y"])

print('-----------------------------------------------------')
# Crea una serie Pandas sencilla a partir de un diccionario:
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

print('-----------------------------------------------------')
# Crear una serie utilizando únicamente datos del "día 1" y del "día 2":
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

print('-----------------------------------------------------')
# Los conjuntos de datos en Pandas suelen ser tablas multidimensionales, llamadas DataFrames.
# Una serie es como una columna, un DataFrame es la tabla completa.
# Crear un DataFrame a partir de dos Series:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)

print('-----------------------------------------------------')
# Cree un Pandas DataFrame simple:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
print('-----------------------------------------------------')
print(df.loc[0])
print('-----------------------------------------------------')
print(df.loc[[0, 1]])

print('-----------------------------------------------------')
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
print('-----------------------------------------------------')
print(df.loc["day2"])

print('-----------------------------------------------------')
# Imprima el DataFrame sin el to_string() método:
df = pd.read_csv('datos.csv')
print(df.to_string()) 

print('-----------------------------------------------------')
# Compruebe el número máximo de filas devueltas en el sistema
print(pd.options.display.max_rows)
print('-----------------------------------------------------')
# Aumente el número máximo de filas para mostrar todo el DataFrame:
pd.options.display.max_rows = 9999
df = pd.read_csv('datos.csv')
print(df) 

print('-----------------------------------------------------')
df = pd.read_json('data.json')
print(df.to_string())

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

# df = pd.DataFrame(data)

# print(df) 
print('-----------------------------------------------------')
# Obtenga una descripción general rápida imprimiendo las primeras 8 filas del DataFrame:
df = pd.read_csv('datos.csv')
print(df.head(8))

print('-----------------------------------------------------')
# Imprima las primeras 5 filas del DataFrame:
df = pd.read_csv('datos.csv')
print(df.head())

print('-----------------------------------------------------')
# Imprima las últimas 5 filas del DataFrame:
print(df.tail()) 

print('-----------------------------------------------------')
print(df.info()) 