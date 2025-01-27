# La regresión múltiple es como la regresión lineal , pero con más de un valor independiente,
#  lo que significa que intentamos predecir un valor en función de dos o más variables.
# Eche un vistazo al conjunto de datos a continuación, que contiene información sobre los automóviles.

# Podemos predecir las emisiones de CO2 de un automóvil en función del tamaño del motor,
# pero con la regresión múltiple podemos introducir más variables, como el peso del automóvil,
# para que la predicción sea más precisa.

import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

# Luego haz una lista de los valores independientes y llama a esta variable X.
# Coloque los valores dependientes en una variable llamada y.

X = df[['Weight', 'Volume']]
y = df['CO2']

# Desde el módulo sklearn utilizaremos el LinearRegression() para crear un objeto de regresión lineal.
# Este objeto tiene un método llamado fit()que toma los valores independientes 
# y dependientes como parámetros y llena el objeto de regresión con datos que describen la relación:
regr = linear_model.LinearRegression()
regr.fit(X, y)

# Ahora tenemos un objeto de regresión que está listo para predecir los valores de CO2 en función del peso 
# y el volumen de un automóvil:
predictedCO2 = regr.predict([[2300, 1300]])

# Hemos pronosticado que un coche con motor de 1,3 litros y un peso de 2.300 kg 
# liberará aproximadamente 107 gramos de CO2 por cada kilómetro recorrido.
print(predictedCO2)


# El coeficiente es un factor que describe la relación con una variable desconocida.
# Ejemplo: si x es una variable, entonces 2x es x sdos veces. xes la variable desconocida 
# y el número 2 es el coeficiente.

# En este caso, podemos preguntar por el valor del coeficiente de peso en relación con el CO2 
# y por el de volumen en relación con el CO2. 
# La(s) respuesta(s) que obtengamos nos indicarán qué ocurriría si aumentamos o 
# disminuimos uno de los valores independientes.

# Imprima los valores de los coeficientes del objeto de regresión:
df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

# La matriz de resultados representa los valores de los coeficientes de peso y volumen.
# Peso: 0,00755095
# Volumen: 0,00780526
# Estos valores nos indican que si el peso aumenta en 1 kg, la emisión de CO2 aumenta en 0,00755095 g.
# Y si el tamaño del motor (volumen) aumenta en 1 cm3 , la emisión de CO2 aumenta en 0,00780526 g.
# Creo que es una suposición acertada, ¡pero probémosla!
# Ya hemos previsto que si un coche con un motor de 1.300 cm3 pesa 2.300 kg, la emisión de CO2 
# será de aproximadamente 107 g.
# ¿Qué pasa si aumentamos el peso en 1000kg?
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)

# Hemos pronosticado que un coche con motor de 1,3 litros y un peso de 3.300 kg 
# liberará aproximadamente 115 gramos de CO2 por cada kilómetro recorrido.
# Lo que demuestra que el coeficiente de 0,00755095 es correcto:
# 107,2087328 + (1000 * 0,00755095) = 114,75968

