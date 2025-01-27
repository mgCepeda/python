# En este capítulo aprenderemos cómo crear una matriz donde los valores se concentran alrededor de un valor dado.
# En teoría de probabilidad, este tipo de distribución de datos se conoce como distribución de datos normal 
# o distribución de datos gaussiana , en honor al matemático Carl Friedrich Gauss, 
# quien ideó la fórmula de esta distribución de datos.

# Una distribución de datos normal típica:
import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()