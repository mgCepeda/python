# El trybloque generará una excepción, porque xno está definido:
try:
  print(x)
except:
  print("An exception occurred")


print('-----------------------------------------------------')
# Imprima un mensaje si el bloque try genera un error NameErrory otro para otros errores:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

print('-----------------------------------------------------')
# En este ejemplo, el trybloque no genera ningún error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print('-----------------------------------------------------')
# El finallybloque, si se especifica, se ejecutará independientemente de si el bloque try genera un error o no.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

print('-----------------------------------------------------')
# Intente abrir y escribir en un archivo que no se puede escribir:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

print('-----------------------------------------------------')
# Genera un error y detiene el programa si x es menor que 0:
# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

print('-----------------------------------------------------')
# Genera un TypeError si x no es un entero:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")