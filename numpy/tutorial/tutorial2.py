from numpy import random
import numpy as np

# Generar un entero aleatorio de 0 a 100:
x = random.randint(100)
print(x)

print('-----------------------------------------------------')
# Generar un flotante aleatorio de 0 a 1:
x = random.rand()
print(x)

print('-----------------------------------------------------')
# Genere una matriz 1-D que contenga 5 números enteros aleatorios del 0 al 100:
x=random.randint(100, size=(5))
print(x)

print('-----------------------------------------------------')
# Genere una matriz 2D con 3 filas, cada fila conteniendo 5 números enteros aleatorios de 0 a 100:
x = random.randint(100, size=(3, 5))
print(x)

print('-----------------------------------------------------')
# Generar una matriz 1-D que contenga 5 flotantes aleatorios:
x = random.rand(5)
print(x)

print('-----------------------------------------------------')
# Genere una matriz 2D con 3 filas, cada fila conteniendo 5 números aleatorios:
x = random.rand(3, 5)
print(x)

print('-----------------------------------------------------')
# Devuelve uno de los valores de una matriz:
x = random.choice([3, 5, 7, 9])
print(x)

print('-----------------------------------------------------')
# Genere una matriz 2-D que consta de los valores del parámetro de matriz (3, 5, 7 y 9):
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

print('-----------------------------------------------------')
# Genere una matriz 1-D que contenga 100 valores, donde cada valor debe ser 3, 5, 7 o 9.
# La probabilidad de que el valor sea 3 se establece en 0,1.
# La probabilidad de que el valor sea 5 se establece en 0,3.
# La probabilidad de que el valor sea 7 se establece en 0,6.
# La probabilidad de que el valor sea 9 se establece en 0.
# La suma de todos los números de probabilidad debe ser 1.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

print('-----------------------------------------------------')
# El mismo ejemplo que el anterior, pero devuelve una matriz 2-D con 3 filas, cada una con 5 valores.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

print('-----------------------------------------------------')
# Mezcla aleatoriamente elementos de la siguiente matriz:
# El shuffle() método realiza cambios en la matriz original.
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

print('-----------------------------------------------------')
# Generar una permutación aleatoria de elementos de la siguiente matriz:
# El permutation() método devuelve una matriz reorganizada (y deja la matriz original sin cambios).
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))