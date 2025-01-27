# Escribir una función que reciba un diccionario con las notas de los alumno de un curso 
# y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

import pandas as pd

alumnos = {
    "alumno1":{
        "nombre": "Juan",
        "asignaturas": {
            "matematicas": 5,
            "lengua": 7,
            "ingles": 3
        }
    },
        "alumno2":{
        "nombre": "Marta",
        "asignaturas": {
            "matematicas": 10,
            "lengua": 10,
            "ingles": 10
        }
    },
        "alumno3":{
        "nombre": "Jonny",
        "asignaturas": {
            "matematicas": 0,
            "lengua": 2,
            "ingles": 0
        }
    },

}

def calcular_estadisticas(alumnos):
    todas_las_notas = []
    
    # Recorrer todos los alumnos y sus asignaturas
    for alumno in alumnos.values():
        for nota in alumno["asignaturas"].values():
            todas_las_notas.append(nota)
    
    notas = pd.Series(todas_las_notas)
    # Calcular la nota mínima, máxima y media
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos
 
# Usar la función con tu diccionario de alumnos
resultados = calcular_estadisticas(alumnos)
print(calcular_estadisticas(alumnos))

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))