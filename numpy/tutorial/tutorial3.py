import numpy as np

# Sin ufunc, podemos usar el método incorporado de Python zip():
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

print('-----------------------------------------------------')
# Con ufunc, podemos utilizar la add()función:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)

print('-----------------------------------------------------')

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print('-----------------------------------------------------')
# Comprueba si una función es una ufunc:
print(type(np.add))

print('-----------------------------------------------------')
# Compruebe el tipo de otra función: concatenate():
print(type(np.concatenate))

print('-----------------------------------------------------')
# Agregue los valores en arr1 a los valores en arr2:
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# Resta los valores en arr2 de los valores en arr1:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# Multiplica los valores en arr1 por los valores en arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# Divida los valores en arr1 con los valores en arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# La power()función eleva los valores de la primera matriz a la potencia de los valores de la segunda matriz 
# y devuelve los resultados en una nueva matriz.
# Eleva los valores en arr1 a la potencia de los valores en arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# Tanto las funciones mod()como remainder()devuelven el resto de los valores de la primera matriz 
# correspondientes a los valores de la segunda matriz, y devuelven los resultados en una nueva matriz.
# Devolver los restos:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.remainder(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# Cociente y módulo
# La divmod()función devuelve tanto el cociente como el módulo. 
# El valor de retorno son dos matrices, la primera matriz contiene el cociente y 
# la segunda matriz contiene el módulo.
# Devuelve el cociente y el módulo:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# Valores absolutos
# Tanto las funciones absolute()como abs()las realizan la misma operación absoluta elemento por elemento, 
# pero debemos usarlas absolute() para evitar confusiones con las funciones integradas de Python.math.abs()
# Devuelve el cociente y el módulo:
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

print('-----------------------------------------------------')
# Truncar elementos de la siguiente matriz:
arr = np.trunc([-3.1666, 3.6667])
print(arr)

# El mismo ejemplo, utilizando fix():
arr = np.fix([-3.1666, 3.6667])
print(arr)

print('-----------------------------------------------------')
# Redondea 3,1666 a 2 decimales:
arr = np.around(3.1666, 2)
print(arr)

print('-----------------------------------------------------')
# entero inferior mas cercano
arr = np.floor([-3.1666, 3.6667])
print(arr)

# entero superior mas cercano
arr = np.ceil([-3.1666, 3.6667])
print(arr)
print('-----------------------------------------------------')

# Encuentra el logaritmo en base 2 de todos los elementos de la siguiente matriz:
# Nota: La arange(1, 10)función devuelve una matriz con números enteros desde 1 (incluido) hasta 10 (no incluido).
arr = np.arange(1, 10)
print(arr)
print(np.log2(arr))

print('-----------------------------------------------------')
# Encuentra el logaritmo en base 10 de todos los elementos de la siguiente matriz:
arr = np.arange(1, 10)
print(np.log10(arr))

print('-----------------------------------------------------')
# Encuentra el logaritmo en la base e de todos los elementos de la siguiente matriz:
arr = np.arange(1, 10)
print(np.log(arr))

# NumPy no proporciona ninguna función para tomar el registro en cualquier base, 
# por lo que podemos usar la frompyfunc()función junto con la función incorporada math.log()
# con dos parámetros de entrada y un parámetro de salida:

from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))

print('-----------------------------------------------------')
# Agregue los valores en arr1 a los valores en arr2:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# Suma los valores en arr1 y los valores en arr2:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)

print('-----------------------------------------------------')
# Realizar la suma en la siguiente matriz sobre el primer eje:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

print('-----------------------------------------------------')
# Realizar la suma acumulativa en la siguiente matriz:
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)

print('-----------------------------------------------------')
# Encuentra el producto de los elementos de esta matriz:
# Devuelve: 24 porque 1*2*3*4 = 24
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)

# Encuentra el producto de los elementos de dos matrices:
# Devuelve: 40320 porque 1*2*3*4*5*6*7*8 = 40320
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)

# Realizar la suma en la siguiente matriz sobre el primer eje:
# Devoluciones: [24 1680]
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)

print('-----------------------------------------------------')
# Tome el producto acumulativo de todos los elementos de la siguiente matriz:
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)

print('-----------------------------------------------------')
# Calcular la diferencia discreta de la siguiente matriz:
# Devuelve: [5 10 -20] porque 15-10=5, 25-15=10 y 5-25=-20
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)

# Calcular la diferencia discreta de la siguiente matriz dos veces:
# Devuelve: [5 -30] porque: 15-10=5, 25-15=10 y 5-25=-20 Y 10-5=5 y -20-10=-30
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)

print('-----------------------------------------------------')
# Encuentra el MinCM de los siguientes dos números:
# Devuelve: 12 porque ese es el mínimo común múltiplo de ambos números (4*3=12 y 6*2=12).
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)

# Encuentra el MinCM de los valores de la siguiente matriz:
# Devuelve: 18 porque ese es el mínimo común múltiplo de los tres números (3*6=18, 6*3=18 y 9*2=18).
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)

# Encuentra el MCM de todos los valores de una matriz donde la matriz contiene todos 
# los números enteros del 1 al 10:
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)

print('-----------------------------------------------------')
# Encuentra el MCD de los siguientes dos números:
# Devuelve: 3 debido a que ese es el número más alto, ambos números se pueden dividir por (6/3=2 y 9/3=3).
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

# Encuentra el MCD para todos los números en la siguiente matriz:
# Devuelve: 4 porque ese es el número más alto por el cual se pueden dividir todos los valores.
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)

print('-----------------------------------------------------')
# Encuentra el valor del seno de PI/2:
x = np.sin(np.pi/2)
print(x)

# Encuentra valores de seno para todos los valores en arr:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

print('-----------------------------------------------------')
# Convierte todos los valores de la siguiente matriz arr a radianes:
# Nota: los valores en radianes son pi/180 * valores en grados.
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

# Convierte todos los valores de la siguiente matriz arr a grados:
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

print('-----------------------------------------------------')
# Encuentra el ángulo de 1.0:
x = np.arcsin(1.0)
print(x)

# Encuentra el ángulo para todos los valores del seno en la matriz.
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

print('-----------------------------------------------------')
# Encuentra las hipotenuas
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)


print('-----------------------------------------------------')
# NumPy proporciona las ufuncs sinh(), cosh()que tanh()toman valores en radianes y
# producen los valores sinh, cosh y tanh correspondientes.
# Encuentra el valor sinh de PI/2:
x = np.sinh(np.pi/2)
print(x)

print('-----------------------------------------------------')
# Encuentra valores cosh para todos los valores en arr:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)

print('-----------------------------------------------------')
# Encuentra el ángulo de 1.0:
x = np.arcsinh(1.0)
print(x)

print('-----------------------------------------------------')
# Encuentra el ángulo para todos los valores de tanh en la matriz:
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)

print('-----------------------------------------------------')
# Podemos usar unique() de NumPy para buscar elementos únicos de cualquier matriz. 
# Por ejemplo, podemos crear una matriz de conjuntos, pero recordemos que las matrices de conjuntos 
# solo deben ser matrices unidimensionales.
# Convierte la siguiente matriz con elementos repetidos en un conjunto:
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

print('-----------------------------------------------------')
# Encuentra la unión de las siguientes dos matrices de conjuntos:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)

print('-----------------------------------------------------')
# Encuentra la intersección de las siguientes dos matrices de conjuntos:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)

print('-----------------------------------------------------')
# Encuentra la diferencia del conjunto 1 y el conjunto 2:
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)


print('-----------------------------------------------------')
# Encuentra la diferencia simétrica del conjunto 1 y el conjunto 2:
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)