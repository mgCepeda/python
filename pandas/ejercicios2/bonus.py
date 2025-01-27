import pandas as pd

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
empleados = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})

# Mostrar por pantalla las filas pares del DataFrame.
empleados_impares = empleados[empleados['employee_id'] % 2 != 0]
resultado = empleados_impares[~empleados_impares['name'].str.startswith('M')]

# Crear una nueva columna 'bono' en el DataFrame original
# empleados['bono'] = empleados['salary'].apply(lambda x: x if x in resultado['salary'].values else 0)

# Calcular el bono utilizando `isin` para verificar si el empleado está en `resultado`
empleados['bono'] = empleados['employee_id'].isin(resultado['employee_id']) * empleados['salary']  # Multiplicamos por salary
print(empleados[['employee_id','bono']])
print("--------------------------------------")
print(empleados)


