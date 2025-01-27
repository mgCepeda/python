
import pandas as pd


datos = {
    'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
    'Ventas':[30500, 35600, 28300, 33900], 
    'Gastos':[22000, 23400, 18100, 20700]
    }
contabilidad = pd.DataFrame(datos)
print(contabilidad)

print("..................................................................................")

import pandas as pd

datos = [
    ['Enero', 30500, 22000],
    ['Febrero', 35600, 23400], 
    ['Marzo', 28300, 18100], 
    ['Abril', 33900,20700]
    ]
contabilidad = pd.DataFrame(datos, columns=['Mes', 'Ventas', 'Gastos'])
print(contabilidad)