import numpy as np
print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

print('-----------------------------------------------------')

arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(type(arr))

print('-----------------------------------------------------')

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])

arr = np.array(
    [[[1, 2, 3], [4, 5, 6]], 
    [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

print('-----------------------------------------------------')
# Imprima el último elemento de la segunda dimensión:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

print('-----------------------------------------------------')
# Cortar los elementos del índice 1 al índice 5 de la siguiente matriz:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

print('-----------------------------------------------------')
# Cortar elementos desde el índice 4 hasta el final de la matriz:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

print('-----------------------------------------------------')
# Rebanar elementos desde el inicio hasta el índice 4 (no incluido):
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

print('-----------------------------------------------------')
# Rebanada desde el índice 3 desde el final hasta el índice 1 desde el final:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

print('-----------------------------------------------------')
# Devuelve todos los demás elementos desde el índice 1 hasta el índice 5:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

print('-----------------------------------------------------')
# Devuelve todos los demás elementos de la matriz completa:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

print('-----------------------------------------------------')
# A partir del segundo elemento, corte los elementos del índice 1 al índice 4 (no incluidos):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

print('-----------------------------------------------------')
# De ambos elementos, devuelve el índice 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

print('-----------------------------------------------------')
# A partir de ambos elementos, corte el índice 1 al índice 4 (no incluido), esto devolverá una matriz 2-D:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

print('-----------------------------------------------------')
# Obtener el tipo de datos de una matriz que contiene cadenas:
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

print('-----------------------------------------------------')
# Crea una matriz con el tipo de datos cadena:
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

print('-----------------------------------------------------')
# Crea una matriz con un tipo de datos entero de 4 bytes:
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# Una cadena no entera como 'a' no se puede convertir en un entero (generará un error):
# arr = np.array(['a', '2', '3'], dtype='i')

print('-----------------------------------------------------')
# Cambie el tipo de datos de flotante a entero usando 'i'como valor de parámetro:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

print('-----------------------------------------------------')
# Cambiar el tipo de datos de entero a booleano:
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

print('-----------------------------------------------------')
# Haga una copia, cambie la matriz original y muestre ambas matrices:
# La copia NO DEBE verse afectada por los cambios realizados en la matriz original.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

print('-----------------------------------------------------')
# Cree una vista, cambie la matriz original y muestre ambas matrices:
# La vista DEBERÍA verse afectada por los cambios realizados en la matriz original.
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

print('-----------------------------------------------------')
# Cree una vista, cambie la vista y muestre ambas matrices:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

print('-----------------------------------------------------')
# Imprima el valor del atributo base para verificar si una matriz posee sus datos o no:
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

print('-----------------------------------------------------')
# Imprima la forma de una matriz 2D:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

print('-----------------------------------------------------')
# Crea una matriz con 5 dimensiones usando ndminun vector con valores 1,2,3,4 y verifica que la última dimensión tenga el valor 4:
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

print('-----------------------------------------------------')
# Convierta la siguiente matriz 1-D con 12 elementos en una matriz 2-D.
# La dimensión más externa tendrá 4 matrices, cada una con 3 elementos:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

print('-----------------------------------------------------')
# Convierta la siguiente matriz 1-D con 12 elementos en una matriz 3-D.
# La dimensión más externa tendrá 2 matrices que contienen 3 matrices, cada una con 2 elementos:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)


print('-----------------------------------------------------')
# Comprueba si la matriz devuelta es una copia o una vista:
# El ejemplo devuelve la matriz original, por lo que es una vista.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)


print('-----------------------------------------------------')
# Convertir una matriz 1D con 8 elementos a una matriz 3D con 2x2 elementos:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

print('-----------------------------------------------------')
# Convierte la matriz en una matriz 1D:
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

print('-----------------------------------------------------')
# Iterar sobre los elementos de la siguiente matriz 1-D:
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

print('-----------------------------------------------------')
# Iterar sobre los elementos de la siguiente matriz 2-D:
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

print('-----------------------------------------------------')
# Iterar sobre cada elemento escalar de la matriz 2-D:
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

print('-----------------------------------------------------')
# Iterar sobre los elementos de la siguiente matriz 3D:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

print('-----------------------------------------------------')
# Iterar hasta los escalares:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)

print('-----------------------------------------------------')
# Iterar a través de la siguiente matriz 3-D:
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)


print('-----------------------------------------------------')
# Iterar a través de la matriz como una cadena:
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


print('-----------------------------------------------------')
# Iterar a través de cada elemento escalar de la matriz 2D omitiendo 1 elemento:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

print('-----------------------------------------------------')
# Enumerar los siguientes elementos de matrices 1D:
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

print('-----------------------------------------------------')
# Enumerar los siguientes elementos de la matriz 2D:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

print('-----------------------------------------------------')
# Unir dos matrices
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

print('-----------------------------------------------------')
# Unir dos matrices 2D a lo largo de filas (eje=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

print('-----------------------------------------------------')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

print('-----------------------------------------------------')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

print('-----------------------------------------------------')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

print('-----------------------------------------------------')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)

print('-----------------------------------------------------')
# Divida la matriz en 3 partes:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

print('-----------------------------------------------------')
# Divida la matriz en 4 partes:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

print('-----------------------------------------------------')
# Acceda a las matrices divididas:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print('-----------------------------------------------------')
# Divida la matriz 2-D en tres matrices 2-D.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print('-----------------------------------------------------')
# Divida la matriz 2-D en tres matrices 2-D.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print('-----------------------------------------------------')
# Divida la matriz 2-D en tres matrices 2-D a lo largo de filas.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print('-----------------------------------------------------')
# Utilice el hsplit()método para dividir la matriz 2-D en tres matrices 2-D a lo largo de filas.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print('-----------------------------------------------------')
# Encuentra los índices donde el valor es 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

print('-----------------------------------------------------')
# Encuentra los índices donde los valores son pares:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

print('-----------------------------------------------------')
# Encuentra los índices donde los valores son impares:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)

print('-----------------------------------------------------')
# Se supone que el searchsorted()método se utiliza en matrices ordenadas.
# Encuentra los índices donde se debe insertar el valor 7:
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

print('-----------------------------------------------------')
# Encuentra los índices donde se debe insertar el valor 7, comenzando desde la derecha:
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

print('-----------------------------------------------------')
# Encuentra los índices donde se deben insertar los valores 2, 4 y 6:
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

print('-----------------------------------------------------')
# Ordenar la matriz:
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

print('-----------------------------------------------------')
# Ordenar la matriz alfabéticamente:
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

print('-----------------------------------------------------')
# Ordenar una matriz booleana:
arr = np.array([True, False, True])
print(np.sort(arr))

print('-----------------------------------------------------')
# Ordenar una matriz 2D:
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

print('-----------------------------------------------------')
# Crea una matriz a partir de los elementos en el índice 0 y 2:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

print('-----------------------------------------------------')
# Cree una matriz de filtros que devolverá solo valores superiores a 42:
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Cree una matriz de filtros que devolverá solo elementos pares de la matriz original:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
filter_arr = []

print('-----------------------------------------------------')
# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

print('-----------------------------------------------------')
# Cree una matriz de filtros que devolverá solo valores superiores a 42:
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print('-----------------------------------------------------')
# Cree una matriz de filtros que devolverá solo elementos pares de la matriz original:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)