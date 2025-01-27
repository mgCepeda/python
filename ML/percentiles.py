# Los percentiles se utilizan en estadística para brindar un número que describe el valor al cual 
# un porcentaje determinado de los valores es inferior.
# Ejemplo: Digamos que tenemos una matriz que contiene las edades de todas las personas que viven en una calle.
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# ¿Qué es el percentil 75? La respuesta es 43, lo que significa que el 75 % de las personas tienen 43 años o menos.

# Utilice el percentile()método NumPy para encontrar los percentiles:

import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)

# ¿Cuál es la edad de la que el 90% de las personas son más jóvenes?
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 90)
print(x)