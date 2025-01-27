# Anteriormente en este tutorial, hemos trabajado con cantidades muy pequeñas de datos en nuestros ejemplos, 
# solo para comprender los diferentes conceptos.
# En el mundo real, los conjuntos de datos son mucho más grandes,
#  pero puede ser difícil recopilar datos del mundo real, al menos en una etapa temprana de un proyecto.
# ¿Cómo podemos obtener grandes conjuntos de datos?
# Para crear grandes conjuntos de datos para pruebas, utilizamos el módulo Python NumPy,
#  que viene con varios métodos para crear conjuntos de datos aleatorios, de cualquier tamaño.

# Crea una matriz que contenga 250 números flotantes aleatorios entre 0 y 5:
import matplotlib.pyplot as plt
import numpy
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)

# Para visualizar el conjunto de datos podemos dibujar un histograma con los datos que hemos recopilado.
# Utilizaremos el módulo Python Matplotlib para dibujar un histograma.
# Dibuje un histograma:
# plt.hist(x, 5)
# plt.show()


# Cree una matriz con 100000 números aleatorios y muéstrelos usando un histograma con 100 barras:
x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()