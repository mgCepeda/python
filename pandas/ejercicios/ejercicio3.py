# Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y 
# devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

import pandas as pd

def ordenar_notas(alumnos):
    todas_las_notas = []
    notas_odenadas= []
    
    # Recorrer todos los alumnos y sus asignaturas
    for alumno in alumnos.values():
        for nota in alumno["asignaturas"].values():
            if nota >= 5:
                todas_las_notas.append(nota)

    todas_las_notas.sort(reverse=True)
    notas = pd.Series(todas_las_notas)
    return notas

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

print(ordenar_notas(alumnos))

print("..................................................................................")

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 5].sort_values(ascending=False)

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(aprobados(notas))