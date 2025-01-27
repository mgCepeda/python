import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# Cómo trazar un diagrama de distribución
# sns.distplot([0, 1, 2, 3, 4, 5])
# plt.show()

# Cómo trazar un diagrama de distribución sin el histograma
# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
# plt.show()

# Generar una distribución normal aleatoria de tamaño 2x3:
# x = random.normal(size=(2, 3))
# print(x)

# # Genere una distribución normal aleatoria de tamaño 2x3 con media de 1 y desviación estándar de 2:
# x = random.normal(loc=1, scale=2, size=(2, 3))
# print(x)

# La curva de una distribución normal también se conoce como curva de campana debido a su forma de campana.
# sns.distplot(random.normal(size=1000), hist=False)
# plt.show()

# La distribución binomial es una distribución discreta .
# Describe el resultado de escenarios binarios, por ejemplo, al lanzar una moneda, saldrá cara o cruz.
# Tiene tres parámetros:
# n- número de ensayos.
# p- probabilidad de ocurrencia de cada ensayo (por ejemplo, para el lanzamiento de una moneda, 0,5 cada uno).
# size- La forma de la matriz devuelta.

# Distribución discreta: la distribución se define en un conjunto separado de eventos, 
# por ejemplo, el resultado del lanzamiento de una moneda es discreto, ya que solo puede ser cara o cruz, 
# mientras que la altura de las personas es continua, ya que puede ser 170, 170,1, 170,11, etc.

# Dados 10 intentos de lanzamiento de moneda, se generan 10 puntos de datos:
# x = random.binomial(n=10, p=0.5, size=10)
# print(x)

# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
# plt.show()

# Diferencia entre distribución normal y binomial
# La principal diferencia es que la distribución normal es continua mientras que la binomial es discreta,
# pero si hay suficientes puntos de datos será bastante similar a la distribución normal con cierta ubicación y
# escala.

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()