# ¿Qué es la desviación estándar?
# La desviación estándar es un número que describe qué tan dispersos están los valores.
# Una desviación estándar baja significa que la mayoría de los números están cerca del valor medio (promedio).
# Una desviación estándar alta significa que los valores están distribuidos en un rango más amplio.
# Ejemplo: Esta vez hemos registrado la velocidad de 7 coches:
# speed = [86,87,88,86,87,85,86]
# La desviación estándar es: 0.9
# Lo que significa que la mayoría de los valores están dentro del rango de 0,9 respecto al valor medio,que es 86,4.

# Hagamos lo mismo con una selección de números con un rango más amplio:
# speed = [32,111,138,28,59,77,97]
# La desviación estándar es: 37.85
# Lo que significa que la mayoría de los valores están dentro del rango de 37,85 respecto al valor medio, que es 77,4.
# Como puede ver, una desviación estándar más alta indica que los valores están distribuidos en un rango más amplio.

# El módulo NumPy tiene un método para calcular la desviación estándar:
# Utilice std()  de NumPy para encontrar la desviación estándar:

import numpy

speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)