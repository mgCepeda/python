# Importa el módulo datetime y muestra la fecha actual:
import datetime

x = datetime.datetime.now()
print(x)


print('-----------------------------------------------------')

# Devuelve el año y el nombre del día de la semana:
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


print('-----------------------------------------------------')
# Crear un objeto de fecha:
x = datetime.datetime(2020, 5, 17)

print(x)

print('-----------------------------------------------------')
# Mostrar el nombre del mes:
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))