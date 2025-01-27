# El término regresión se utiliza cuando se intenta encontrar la relación entre variables.
# En el aprendizaje automático y en el modelado estadístico, esa relación se utiliza para predecir 
# el resultado de eventos futuros.

# La regresión lineal utiliza la relación entre los puntos de datos para dibujar una línea recta a través
# de todos ellos.
# Esta línea se puede utilizar para predecir valores futuros.

# Python tiene métodos para encontrar una relación entre puntos de datos y 
# para dibujar una línea de regresión lineal. 
# Le mostraremos cómo utilizar estos métodos en lugar de recurrir a la fórmula matemática.

# En el siguiente ejemplo, el eje x representa los años, y el eje y la velocidad. 
# Hemos registrado la edad y la velocidad de 13 automóviles cuando pasaban por una cabina de peaje. 
# Veamos si los datos que hemos recopilado se pueden utilizar en una regresión lineal:

# Importar scipyy dibujar la línea de regresión lineal:

import matplotlib.pyplot as plt
from scipy import stats

# Crea las matrices que representan los valores de los ejes x e y:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Ejecute un método que devuelva algunos valores clave importantes de la regresión lineal:
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Cree una función que utilice los valores slope y intercept devolver un nuevo valor. 
# Este nuevo valor representa en qué parte del eje y se colocará el valor x correspondiente:
def myfunc(x):
  return slope * x + intercept

# Ejecute cada valor de la matriz x a través de la función. 
# Esto generará una nueva matriz con nuevos valores para el eje y:
mymodel = list(map(myfunc, x))

# Dibuje el diagrama de dispersión original:
plt.scatter(x, y)

# Dibuje la línea de regresión lineal:
plt.plot(x, mymodel)

# Mostrar el diagrama:
plt.show()