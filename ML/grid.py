# La mayoría de los modelos de aprendizaje automático contienen parámetros que se pueden ajustar para 
# la forma en que aprende el modelo.
# Por ejemplo, el modelo de regresión logística, de sklearn, tiene un parámetro Cque controla la regularización,
# lo que afecta la complejidad del modelo.

# ¿Cómo elegimos el mejor valor para C? El mejor valor depende de los datos utilizados para entrenar el modelo.

# Un método consiste en probar distintos valores y luego elegir el valor que dé la mejor puntuación. 
# Esta técnica se conoce como búsqueda en cuadrícula . 
# Si tuviéramos que seleccionar los valores de dos o más parámetros, 
# todas las combinaciones de los conjuntos de valores, formando así una cuadrícula de valores.

# Antes de comenzar con el ejemplo, es bueno saber qué hace el parámetro que estamos modificando. 
# Los valores más altos de C indican al modelo que los datos de entrenamiento se asemejan 
# a la información del mundo real, lo que otorga un mayor peso a los datos de entrenamiento,
# mientras que los valores más bajos de C hacen lo contrario.

# Primero veamos qué tipo de resultados podemos generar sin una búsqueda de cuadrícula utilizando 
# solo los parámetros base.
# Para comenzar, primero debemos cargar el conjunto de datos con el que trabajaremos.

from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# Para comenzar, primero debemos cargar el conjunto de datos con el que trabajaremos.
iris = datasets.load_iris()

# A continuación, para crear el modelo debemos tener un conjunto de variables independientes X y
# una variable dependiente y.
X = iris['data']
y = iris['target']

# Creando el modelo, estableciendo max_iter en un valor más alto para garantizar que el modelo encuentre un resultado.
# Tenga en cuenta que el valor predeterminado para Cen un modelo de regresión logística es 1, 
# lo compararemos más adelante.
# En el siguiente ejemplo, observamos el conjunto de datos del iris e
# intentamos entrenar un modelo con valores variables C en regresión logística.
logit = LogisticRegression(max_iter = 10000)

# Después de crear el modelo, debemos ajustarlo a los datos.
print(logit.fit(X,y))

# Para evaluar el modelo ejecutamos el método de puntuación.
print(logit.score(X,y))

# Seguiremos los mismos pasos que antes excepto que esta vez estableceremos un rango de valores para C.
# Saber qué valores establecer para los parámetros buscados requerirá una combinación de conocimiento 
# del dominio y práctica.
# Dado que el valor predeterminado para C es 1, estableceremos un rango de valores que lo rodee

C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]

# A continuación, crearemos un bucle for para cambiar los valores C y evaluar el modelo con cada cambio.
# Primero crearemos una lista vacía para almacenar la puntuación.
scores = []

# Para cambiar los valores de Cdebemos recorrer el rango de valores y actualizar el parámetro cada vez.
for choice in C:
  logit.set_params(C=choice)
  logit.fit(X, y)
  scores.append(logit.score(X, y))

# Con las puntuaciones almacenadas en una lista, podemos evaluar cuál C es la mejor opción.
print(scores)

# Podemos ver que los valores más bajos de C tuvieron un peor desempeño que el parámetro base de 1.
# Sin embargo, a medida que aumentamos el valor de C el 1.75 modelo experimentó una mayor precisión.
# Parece que aumentar C más allá de esta cantidad no ayuda a aumentar la precisión del modelo. 