# # En el ejemplo, una persona intentará decidir si debe ir a un espectáculo de comedia o no.
# # Afortunadamente, nuestra persona de ejemplo se registró cada vez que hubo un espectáculo de comedia en la ciudad,
# # y registró cierta información sobre el comediante, y también registró si fue o no.
# import sys
# import matplotlib
# matplotlib.use('Agg')
# import pandas
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt

# # Leer e imprimir el conjunto de datos:
# df = pandas.read_csv("dataArbol.csv")
# # print(df)

# # Para crear un árbol de decisiones, todos los datos deben ser numéricos.
# # Tenemos que convertir las columnas no numéricas 'Nationality' y 'Go' en valores numéricos.
# # Pandas tiene un map()método que toma un diccionario con información sobre cómo convertir los valores.
# # {'UK': 0, 'USA': 1, 'N': 2}
# # Significa convertir los valores 'UK' a 0, 'EE. UU.' a 1 y 'N' a 2.

# # Convertir valores de cadena en valores numéricos:
# d = {'UK': 0, 'USA': 1, 'N': 2}
# df['Nationality'] = df['Nationality'].map(d)
# d = {'YES': 1, 'NO': 0}
# df['Go'] = df['Go'].map(d)

# # print(df)

# # Luego tenemos que separar las columnas de características de la columna de destino .
# # Las columnas de características son las columnas con las que usaremos para predecir, 
# # y la columna de destino es la columna con los valores que intentamos predecir.

# # X es la columna de características, y es la columna de destino:
# features = ['Age', 'Experience', 'Rank', 'Nationality']
# X = df[features]
# y = df['Go']

# print(X)
# print(y)

import pandas
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Cargar datos
df = pandas.read_csv("dataArbol.csv")

# Mapear las columnas 'Nationality' y 'Go' a valores numéricos
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# Definir las características (features) y la variable objetivo (target)
features = ['Nationality', 'Age', 'Experience', 'Rank']
X = df[features]
y = df['Go']

# Crear y entrenar el modelo de árbol de decisión
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# # Dibujar el árbol de decisión
# plt.figure(figsize=(12, 8))
# plot_tree(dtree, feature_names=features, class_names=['NO', 'YES'], filled=True)

# # Mostrar el gráfico en pantalla
# plt.show()

# Rank <= 6.5significa que cada comediante con un rango de 6.5 o menor seguirá la Trueflecha (hacia la izquierda),
# y el resto seguirá la Falseflecha (hacia la derecha).

# gini = 0.497se refiere a la calidad de la división, y siempre es un número entre 0,0 y 0,5,
# donde 0,0 significaría que todas las muestras obtuvieron el mismo resultado 
# y 0,5 significaría que la división se realiza exactamente en el medio.

# samples = 13significa que quedan 13 comediantes en este punto de la decisión, lo cual son todos,
# ya que este es el primer paso.

# value = [6, 7]significa que de estos 13 comediantes, 6 obtendrán un "NO" y 7 obtendrán un "GO".

# coeficiente de gini
# Hay muchas formas de dividir las muestras, en este tutorial utilizamos el método GINI.
# El método Gini utiliza esta fórmula:
# Gini = 1 - (x/n)2 - (y/n)2
# Donde x es el número de respuestas positivas ("GO"), n es el número de muestras y 
# y es el número de respuestas negativas ("NO"), lo que nos da este cálculo:
# 1 - (7 / 13)2 - (6 / 13)2 = 0.497

# El siguiente paso contiene dos casillas, una para los comediantes con un 'Rank' de 6.5 o menos, 
# y otra para el resto.

# Cierto - 5 comediantes terminan aquí:
# gini = 0.0significa que todas las muestras obtuvieron el mismo resultado.
# samples = 5 significa que quedan 5 comediantes en esta rama (5 comediantes con un rango de 6.5 o inferior).
# value = [5, 0]significa que 5 obtendrá un "NO" y 0 obtendrá un "GO".

# Falso - 8 Comediantes Continúan:
# Nacionalidad
# Nationality <= 0.5 significa que los comediantes con un valor de nacionalidad menor a 0,5 
# seguirán la flecha hacia la izquierda (lo que significa todos los del Reino Unido), 
# y el resto seguirá la flecha hacia la derecha.
# gini = 0.219 significa que aproximadamente el 22% de las muestras irían en una dirección.
# samples = 8 significa que quedan 8 comediantes en esta rama (8 comediantes con un rango superior a 6.5).
# value = [1, 7]significa que de estos 8 comediantes, 1 obtendrá un "NO" y 7 obtendrán un "GO"
# ... etc

# Podemos utilizar el árbol de decisiones para predecir nuevos valores.
# Ejemplo: ¿Debería ir a ver un espectáculo protagonizado por un comediante estadounidense de 40 años,
# con 10 años de experiencia y un ranking de comedia de 7?
print(dtree.predict([[40, 10, 7, 1]]))


