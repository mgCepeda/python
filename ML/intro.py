# El aprendizaje automático hace que la computadora aprenda estudiando datos y estadísticas.
# El aprendizaje automático es un paso en la dirección de la inteligencia artificial (IA).
# El aprendizaje automático es un programa que analiza datos y aprende a predecir el resultado.

# En Machine Learning (y en matemáticas) a menudo hay tres valores que nos interesan:

# Media - El valor promedio
# Mediana : El valor del punto medio
# Moda - El valor más común
import numpy


# Utilice el método NumPy mean()para encontrar la velocidad promedio:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

# Utilice el método NumPy median()para encontrar el valor medio:
x = numpy.median(speed)
print(x)

# Si hay dos números en el medio, divide la suma de esos números por dos. (86 + 87) / 2 = 86.5
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

# Utilice el mode()método SciPy para encontrar el número que aparece con más frecuencia
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)