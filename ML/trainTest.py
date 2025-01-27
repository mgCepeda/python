# En Machine Learning creamos modelos para predecir el resultado de ciertos eventos, 
# como en el capítulo anterior donde predijimos la emisión de CO2 de un automóvil cuando conocíamos el peso
# y el tamaño del motor.
# Para medir si el modelo es suficientemente bueno, podemos utilizar un método llamado train/test.

# train/test es un método para medir la precisión de su modelo.
# Se llama Entrenamiento/Prueba porque divide el conjunto de datos en dos conjuntos: 
# un conjunto de entrenamiento y un conjunto de prueba.
# 80% para entrenamiento y 20% para pruebas.

# Entrenar el modelo significa crear el modelo.
# Probar el modelo significa probar la precisión del modelo.

# Comience con un conjunto de datos que desee probar.
# Nuestro conjunto de datos ilustra 100 clientes en una tienda y sus hábitos de compra.

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
from sklearn.metrics import r2_score

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# plt.scatter(x, y)
# plt.show()

# El eje x representa el número de minutos antes de realizar una compra.
# El eje y representa la cantidad de dinero gastada en la compra.


# El conjunto de entrenamiento debe ser una selección aleatoria del 80% de los datos originales.
# El conjunto de prueba debe ser el 20% restante.

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# plt.scatter(train_x, train_y)
# plt.show()

# Para asegurarnos de que el conjunto de pruebas no sea completamente diferente,
# también echaremos un vistazo al conjunto de pruebas.

# plt.scatter(test_x, test_y)
# plt.show()

# ¿Cómo se ve el conjunto de datos? En mi opinión, creo que el mejor ajuste sería una regresión polinómica ,
# así que tracemos una línea de regresión polinómica.
# Para dibujar una línea a través de los puntos de datos, utilizamos el plot()método del módulo matplotlib:

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
# plt.show()

r2 = r2_score(train_y, mymodel(train_x))

# Nota: El resultado 0,799 muestra que existe una relación aceptable.
print(r2)

# Ahora hemos creado un modelo que está bien, al menos en lo que respecta a los datos de entrenamiento.
# Ahora queremos probar el modelo con los datos de prueba también, para ver si nos da el mismo resultado.
r2 = r2_score(test_y, mymodel(test_x))
# Nota: El resultado 0,809 muestra que el modelo también se ajusta al conjunto de pruebas 
# y estamos seguros de que podemos usar el modelo para predecir valores futuros.
print(r2)

# Ahora que hemos establecido que nuestro modelo es correcto, podemos comenzar a predecir nuevos valores.
# ¿Cuánto dinero gastará un cliente que compra si permanece en la tienda durante 5 minutos?
print(mymodel(5))