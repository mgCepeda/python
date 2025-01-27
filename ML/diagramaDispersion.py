# Un diagrama de dispersión es un diagrama donde cada valor del conjunto de datos está representado por un punto.
# El módulo Matplotlib tiene un método para dibujar gráficos de dispersión, 
# necesita dos matrices de la misma longitud, una para los valores del eje x y otra para los valores del eje y:


# La matriz x representa los años de cada coche.
# La matriz  yrepresenta la velocidad de cada automóvil.
# Utilice el scatter()método para dibujar un diagrama de dispersión:
import matplotlib.pyplot as plt
import numpy

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# plt.scatter(x, y)
# plt.show()

# El eje x representa las edades y el eje y representa las velocidades.
# Lo que podemos leer en el diagrama es que los dos autos más rápidos tenían 2 años y el auto más lento tenía 12 años.
# Nota: Parece que cuanto más nuevo es el coche, más rápido va, pero eso podría ser una coincidencia, 
# después de todo sólo registramos 13 coches.


# Distribuciones de datos aleatorios
# En el aprendizaje automático, los conjuntos de datos pueden contener miles o incluso millones de valores.
# Es posible que no tengas datos del mundo real cuando estés probando un algoritmo, 
# es posible que tengas que usar valores generados aleatoriamente.
# Como aprendimos en el capítulo anterior, ¡el módulo NumPy puede ayudarnos con eso!
# Creemos dos matrices que contengan 1000 números aleatorios de una distribución de datos normal.
# La primera matriz tendrá la media establecida en 5,0 con una desviación estándar de 1,0.
# La segunda matriz tendrá la media establecida en 10,0 con una desviación estándar de 2,0:

# Un diagrama de dispersión con 1000 puntos:

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()

# Podemos ver que los puntos se concentran alrededor del valor 5 en el eje x y 10 en el eje y.
# También podemos ver que la dispersión es mayor en el eje y que en el eje x.