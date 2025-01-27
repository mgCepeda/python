
import mymodule

mymodule.greeting("Jonathan")

print('-----------------------------------------------------')

a = mymodule.person1["age"]
print(a)

print('-----------------------------------------------------')

# Crear un alias para mymoduleel llamado mx:
import mymodule as mx

a = mx.person1["age"]
print(a)


print('-----------------------------------------------------')
# Importar y utilizar el platformmódulo:
import platform

x = platform.system()
print(x)

print('-----------------------------------------------------')
# Enumere todos los nombres definidos que pertenecen al módulo de la plataforma:
import platform

x = dir(platform)
print(x)

print('-----------------------------------------------------')
# Importe únicamente el diccionario person1 del módulo:
from mymodule import person1

print (person1["age"])