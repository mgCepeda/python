# Limpieza de datos
# La limpieza de datos significa corregir datos erróneos en su conjunto de datos.

# Los datos erróneos podrían ser:
#     Celdas vacías
#     Datos en formato incorrecto
#     Datos erróneos
#     Duplicados

# El conjunto de datos contiene algunas celdas vacías ("Fecha" en la fila 22 y "Calorías" en las filas 18 y 28).
# El conjunto de datos contiene un formato incorrecto ("Fecha" en la fila 26).
# El conjunto de datos contiene datos incorrectos ("Duración" en la fila 7).
# El conjunto de datos contiene duplicados (filas 11 y 12).

import pandas as pd

# Devolver un nuevo marco de datos sin celdas vacías:
# df = pd.read_csv('data.csv')
# print(df.to_string())
# print('-----------------------------------------------------')
# new_df = df.dropna()
# print(new_df.to_string())
# print('-----------------------------------------------------')

# Nota: De forma predeterminada, el dropna()método devuelve un nuevo DataFrame y no cambiará el original.
# Si desea cambiar el DataFrame original, utilice el inplace = Trueargumento:
# Eliminar todas las filas con valores NULL:

# df = pd.read_csv('data.csv')
# df.dropna(inplace = True)
# print(df.to_string())

print('-----------------------------------------------------')
# Reemplazar valores vacíos
# Otra forma de tratar las celdas vacías es insertar un nuevo valor en su lugar.
# De esta manera no tendrás que eliminar filas enteras sólo porque hay algunas celdas vacías.
# El fillna()método nos permite reemplazar celdas vacías con un valor:
# Reemplace los valores NULL con el número 130:

# df = pd.read_csv('data.csv')
# df.fillna(130, inplace = True)
# print(df.to_string())

print('-----------------------------------------------------')
# Reemplazar solo las columnas especificadas
# El ejemplo anterior reemplaza todas las celdas vacías en todo el marco de datos.
# Para reemplazar solo valores vacíos para una columna, especifique el nombre de la columna para el DataFrame:
# Reemplace los valores NULL en las columnas "Calorías" con el número 130:

# df = pd.read_csv('data.csv')
# df["Calories"].fillna(130, inplace = True)
# print(df.to_string())
print('-----------------------------------------------------')

# Media = valor promedio (la suma de todos los valores dividida por el número de valores).
# Calcula la MEDIA y reemplaza cualquier valor vacío con ella:
# df = pd.read_csv('data.csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)
# print(df.to_string())

print('-----------------------------------------------------')
# Mediana = el valor en el medio, después de haber ordenado todos los valores en orden ascendente.
# Calcula la MEDIANA y reemplaza cualquier valor vacío con ella:
# df = pd.read_csv('data.csv')
# x = df["Calories"].median()
# df["Calories"].fillna(x, inplace = True)
# print(df.to_string())

print('-----------------------------------------------------')
# Moda = el valor que aparece con mayor frecuencia.
# Calcula la MODA y reemplaza cualquier valor vacío con ella:
# df = pd.read_csv('data.csv')
# x = df["Calories"].mode()[0]
# df["Calories"].fillna(x, inplace = True)
# print(df.to_string())

print('-----------------------------------------------------')

# df = pd.read_csv('data.csv')
# df.dropna(subset=['Date'], inplace = True)
# # df['Date'] = pd.to_datetime(df['Date']) no funciona
# print(df.to_string())

print('-----------------------------------------------------')
# Establezca "Duración" = 45 en la fila 7:
# df = pd.read_csv('data.csv')
# df.loc[7,'Duration'] = 45
# print(df.to_string())

print('-----------------------------------------------------')
# Recorrer todos los valores en la columna "Duración".
# Si el valor es mayor que 120, configúrelo en 120:
# df = pd.read_csv('data.csv')

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120

# print(df.to_string())

print('-----------------------------------------------------')
# Eliminar filas donde "Duración" sea mayor a 120:
# df = pd.read_csv('data.csv')

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)

# #remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy
# print(df.to_string())


print('-----------------------------------------------------')
df = pd.read_csv('data.csv')
print(df.duplicated())

df.drop_duplicates(inplace = True)
print(df.to_string())

print('-----------------------------------------------------')




