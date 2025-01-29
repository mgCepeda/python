# La regresión logística tiene como objetivo resolver problemas de clasificación 
# y lo hace prediciendo resultados categóricos, a diferencia de la regresión lineal 
# que predice un resultado continuo.

# En el caso más simple hay dos resultados, lo que se denomina binomial,
# un ejemplo de lo cual es predecir si un tumor es maligno o benigno.
# Otros casos tienen más de dos resultados para clasificar, en este caso se denomina multinomial. 
# Un ejemplo común de regresión logística multinomial sería predecir la clase de una flor de iris 
# entre 3 especies diferentes.

# Aquí utilizaremos una regresión logística básica para predecir una variable binomial. 
# Esto significa que solo tiene dos resultados posibles.
import numpy
from sklearn import linear_model

# Almacene las variables independientes en X.
# Almacene la variable dependiente en y.
# A continuación se muestra un conjunto de datos de muestra:

#X represents the size of a tumor in centimeters.
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)

#Note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.
#y represents whether or not the tumor is cancerous (0 for "No", 1 for "Yes").
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Desde el módulo sklearn utilizaremos el método LogisticRegression() para crear un objeto de regresión logística.
# Este objeto tiene un método llamado fit()que toma los valores independientes y dependientes como parámetros 
# y llena el objeto de regresión con datos que describen la relación:

logr = linear_model.LogisticRegression()
logr.fit(X,y)

# Ahora tenemos un objeto de regresión logística que está listo para determinar 
# si un tumor es canceroso en función de su tamaño:
predicted = logr.predict(numpy.array([3.46]).reshape(-1,1))
# Hemos predicho que un tumor con un tamaño de 3,46 mm no será canceroso.
print(predicted)

# En la regresión logística, el coeficiente es el cambio esperado en las probabilidades logarítmicas 
# de tener el resultado por unidad de cambio en X.
# Esto no es muy intuitivo de entender, así que vamos a usarlo para crear algo que tenga más sentido.
log_odds = logr.coef_
odds = numpy.exp(log_odds)
# Esto nos dice que a medida que el tamaño de un tumor aumenta en 1 mm, 
# las probabilidades de que sea un tumor canceroso aumentan 4 veces.
print(odds)

# Los valores del coeficiente y la intersección se pueden utilizar para encontrar
# la probabilidad de que cada tumor sea canceroso.

# Cree una función que utilice los valores de coeficiente e intersección del modelo para devolver un nuevo valor.
# Este nuevo valor representa la probabilidad de que la observación dada sea un tumor:

def logit2prob(logr,x):
  log_odds = logr.coef_ * x + logr.intercept_
  odds = numpy.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)

# 3,78 0,61 La probabilidad de que un tumor con un tamaño de 3,78 cm sea canceroso es del 61%.
# 2.44 0.19 La probabilidad de que un tumor con un tamaño de 2,44 cm sea canceroso es del 19%.
# 2.09 0.13 La probabilidad de que un tumor con un tamaño de 2,09 cm sea canceroso es del 13%.
print(logit2prob(logr, X))