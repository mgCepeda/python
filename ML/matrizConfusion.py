# Es una tabla que se utiliza en problemas de clasificación para evaluar dónde se cometieron errores en el modelo.
# Las filas representan las clases reales a las que deberían haber pertenecido los resultados,
# mientras que las columnas representan las predicciones que hemos realizado. 
# Con esta tabla es fácil ver qué predicciones son erróneas.

# Las matrices de confusión se pueden crear mediante predicciones realizadas a partir de una regresión logística.
# Por ahora generaremos valores reales y previstos utilizando NumPy:

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

# A continuación tendremos que generar los números para los valores "reales" y "previstos".
actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

# Para crear la matriz de confusión necesitamos importar métricas del módulo sklearn.
# Una vez importadas las métricas, podemos utilizar la función de matriz de confusión en nuestros valores reales 
# y previstos.
confusion_matrix = metrics.confusion_matrix(actual, predicted)

# Para crear una representación visual más interpretable, necesitamos convertir la tabla 
# en una visualización de matriz de confusión.
# cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

# Finalmente, para mostrar la gráfica podemos utilizar las funciones plot() y show() de pyplot.
# cm_display.plot()
# plt.show()

# La Matriz de Confusión creada tiene cuatro cuadrantes diferentes:

# Verdadero negativo (cuadrante superior izquierdo)
# Falso positivo (cuadrante superior derecho)
# Falso negativo (cuadrante inferior izquierdo)
# Verdadero positivo (cuadrante inferior derecho)

# Verdadero significa que los valores se predijeron con precisión,
# Falso significa que hubo un error o una predicción incorrecta.

# Ahora que hemos creado una matriz de confusión, 
# podemos calcular diferentes medidas para cuantificar la calidad del modelo.

# La matriz nos proporciona muchas métricas útiles que nos ayudan a evaluar nuestro modelo de clasificación.
# Las diferentes medidas incluyen: 
# exactitud: La precisión mide la frecuencia con la que el modelo es correcto.
# (Verdadero positivo + Verdadero negativo) / Predicciones totales
Accuracy = metrics.accuracy_score(actual, predicted)

# precisión: De los positivos previstos, ¿qué porcentaje es realmente positivo?
# Verdadero positivo / (Verdadero positivo + Falso positivo)
# La precisión no evalúa los casos negativos predichos correctamente:
Precision = metrics.precision_score(actual, predicted)

# sensibilidad (Recall): De todos los casos positivos, ¿qué porcentaje se prevé positivo?
# La sensibilidad (a veces llamada Recall) mide qué tan bueno es el modelo para predecir resultados positivos.
# Esto significa que analiza los verdaderos positivos y los falsos negativos 
# (que son positivos que se han predicho incorrectamente como negativos).
# Verdadero positivo / (Verdadero positivo + falso negativo)
# La sensibilidad es útil para comprender qué tan bien el modelo predice que algo es positivo:
Sensitivity_recall = metrics.recall_score(actual, predicted)

# especificidad: ¿Qué tan bien es el modelo para predecir resultados negativos?
# La especificidad es similar a la sensibilidad, pero la analiza desde la perspectiva de los resultados negativos.
# Verdadero negativo / (Verdadero negativo + Falso positivo)
# Dado que es exactamente lo opuesto a Recall, utilizamos la función recall_score,
#  tomando la etiqueta de posición opuesta:
Specificity = metrics.recall_score(actual, predicted, pos_label=0)

# puntuación F es la “media armónica” de precisión y sensibilidad.
# Considera tanto casos falsos positivos como falsos negativos y es bueno para conjuntos de datos desequilibrados.
# 2 * ((Precisión * Sensibilidad) / (Precisión + Sensibilidad))
# Esta puntuación no tiene en cuenta los valores negativos verdaderos:
F1_score = metrics.f1_score(actual, predicted)

print(f"Accuracy: {Accuracy}\nPrecision: {Precision}\nSensitivity_recall: {Sensitivity_recall}\nSpecificity: {Specificity}\nF1_score: {F1_score}")


