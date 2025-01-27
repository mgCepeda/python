# Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
# una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

import pandas as pd


def calcular_balance(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()

def balance_por_mes(contabilidad):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    return contabilidad[['Mes', 'Balance']]


datos = {
    'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
    'Ventas':[30500, 35600, 28300, 33900], 
    'Gastos':[22000, 23400, 18100, 20700]
    }
contabilidad = pd.DataFrame(datos)
print(calcular_balance(contabilidad, ['Enero','Marzo']))

print(balance_por_mes(contabilidad))