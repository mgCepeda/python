# Cuando los datos tienen valores diferentes e incluso unidades de medida diferentes,
# puede resultar difícil compararlos. ¿Qué son los kilogramos en comparación con los metros? 
# ¿O la altitud en comparación con el tiempo?

# La respuesta a este problema es el escalamiento.
# Podemos escalar los datos para obtener nuevos valores que sean más fáciles de comparar.

# Eche un vistazo a la tabla a continuación, es el mismo conjunto de datos que usamos en el capítulo
# de regresión múltiple , pero esta vez la columna de volumen contiene valores en litros en lugar de cm3
# (1,0 en lugar de 1000).

# Puede ser difícil comparar el volumen 1.0 con el peso 790, pero si los escalamos a ambos en valores comparables,
# podemos ver fácilmente cuánto es un valor en comparación con el otro.
# Existen diferentes métodos para escalar datos, en este tutorial utilizaremos un método llamado estandarización.

# El método de estandarización utiliza esta fórmula:

# z = (x - u) / s

# Donde z es el nuevo valor, x es el valor original, u es la media y s es la desviación estándar.
# Si toma la columna de peso del conjunto de datos anterior, el primer valor es 790 y el valor escalado será:

# (790 - 1292.23) / 238.74 = -2.1
# Si toma la columna de volumen del conjunto de datos anterior, el primer valor es 1.0 y el valor escalado será:

# (1.0 - 1.61) / 0.38 = -1.59

# Ahora puedes comparar -2,1 con -1,59 en lugar de comparar 790 con 1,0.
# No es necesario que haga esto manualmente, el módulo sklearn de Python 
# tiene un método llamado StandardScaler() que devuelve un objeto Scaler con métodos 
# para transformar conjuntos de datos.

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("dataLitros.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

print(scaledX)

# Predecir los valores de CO2
# La tarea del capítulo de Regresión Múltiple era predecir la emisión de CO2 de un automóvil cuando 
# solo se conocía su peso y volumen.
# Cuando se escala el conjunto de datos, tendrás que usar la escala al predecir valores:

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)