# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. 
# Escribir un programa con los siguientes requisitos:
# 1 .Generar un DataFrame con los datos del fichero.
import pandas as pd

df = pd.read_csv('titanic.csv', index_col=0)
print(df)
print('-----------------------------------------------------')

# 2 .Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, 
# los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print('Dimensiones:', df.shape)
print('Número de elemntos:', df.size)
print('Nombres de columnas:', df.columns)
print('Nombres de filas:', df.index)
print('Tipos de datos:\n', df.dtypes)
print('Primeras 10 filas:\n', df.head(10))
print('Últimas 10 filas:\n', df.tail(10))
print('-----------------------------------------------------')

# Mostrar por pantalla los datos del pasajero con identificador 148.
print(df.loc[148])
print('-----------------------------------------------------')

# Mostrar por pantalla las filas pares del DataFrame.
print(df.iloc[range(1,df.shape[0],2)])
print('-----------------------------------------------------')

# Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(df[df["Pclass"]==1]['Name'].sort_values())
print('-----------------------------------------------------')
# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print(df['Survived'].value_counts(normalize=True) * 100)
print('-----------------------------------------------------')
# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
print(df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100)
print('-----------------------------------------------------')
# Eliminar del DataFrame los pasajeros con edad desconocida.
df.dropna(subset=['Age'], inplace = True)
print(df)
print('-----------------------------------------------------')

# Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print(df.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])
print('-----------------------------------------------------')

# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df['Young'] = df['Age'] < 18
print(df['Young'].to_string())
print('-----------------------------------------------------')

# Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print(df.groupby(['Pclass','Young'])['Survived'].value_counts(normalize=True) * 100)