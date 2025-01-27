# Si sus puntos de datos claramente no se ajustan a una regresión lineal 
# (una línea recta a través de todos los puntos de datos), podría ser ideal para la regresión polinomial.

# La regresión polinomial, al igual que la regresión lineal,
# utiliza la relación entre las variables x e y para encontrar la mejor manera de dibujar una línea 
# a través de los puntos de datos.


# Python tiene métodos para encontrar una relación entre puntos de datos y para dibujar una línea de regresión polinómica.
# Le mostraremos cómo utilizar estos métodos en lugar de recurrir a la fórmula matemática.
# En el siguiente ejemplo, hemos registrado 18 automóviles cuando pasaban por un peaje determinado.
# Hemos registrado la velocidad del vehículo y la hora del día (hora) en que se produjo el adelantamiento.
# El eje x representa las horas del día y el eje y representa la velocidad:

import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# NumPy tiene un método que nos permite hacer un modelo polinomial:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Luego especifica cómo se mostrará la línea, comenzamos en la posición 1 y terminamos en la posición 22:
myline = numpy.linspace(1, 22, 100)

# Dibuje el diagrama de dispersión:
# plt.scatter(x, y)

# # Dibuje la línea de regresión polinomial:
# plt.plot(myline, mymodel(myline))

# # Mostrar el diagrama:
# plt.show()


# R-cuadrado
# Es importante saber qué tan buena es la relación entre los valores de los ejes x e y, 
# si no hay relación, la regresión polinomial no se puede utilizar para predecir nada.

# La relación se mide con un valor llamado r-cuadrado.
# El valor r-cuadrado varía de 0 a 1, donde 0 significa que no hay relación y 1 significa que hay una relación del 100%.

# Python y el módulo Sklearn calcularán este valor por usted,
# todo lo que tiene que hacer es introducirle las matrices x e y:

# ¿Qué tan bien encajan mis datos en una regresión polinomial?
# Nota: El resultado 0,94 muestra que existe una muy buena relación 
# y podemos utilizar la regresión polinomial en futuras predicciones.
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

# Ahora podemos utilizar la información que hemos reunido para predecir valores futuros.
# Ejemplo: Intentemos predecir la velocidad de un automóvil que pasa por el peaje alrededor de las 17:00:

speed = mymodel(17)
print(speed)

# Creemos un ejemplo en el que la regresión polinomial no sería el mejor método para predecir valores futuros.
# Estos valores para los ejes x e y deberían dar como resultado un ajuste muy malo para la regresión polinomial:

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

print(r2_score(y, mymodel(x)))
# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()