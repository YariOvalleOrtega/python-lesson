from typing import ValuesView


students = {'a': {'name':'Juan','notas':[3.1,4.2,4,3.9,3.2]}, 'j': {'name':'Jenny','notas':[4,3.7,4,4,4.2]},\
        'c': {'name':'Ana','notas':[4.1,4.7,4.1,4.9,4.2]}, 'y': {'name':'Pedro','notas':[4,3.7,4,4,4.2]},\
            'x': {'name':'Pablo','notas':[4,3.3,3.4,3.2,3.2]}, 'l': {'name':'Carlos','notas':[3.4,3.8,4.2,4,4.1]},\
                'v': {'name':'Maria','notas':[4.8,4.7,4.6,4.9,4.8]}, 'r': {'name':'Luisa','notas':[4.8,4.7,4.5,4.5,4.9]},\
                    'b': {'name':'Mario','notas':[2.4,3.2,3.1,3.4,4.2]}, 'g': {'name':'Fabio','notas':[2.4,3.2,3.1,3.4,4.2]}}

#el promedio más alto high_average
#el promedio mas bajo low_average
#la nota más alta de todas
#la nota mas baja de todas
# True o False si hay notas repetidas


#PROMEDIO MÁS ALTO

def high_average():
    promedio = 0.0
    estudiante = {}
    for promedioalto in students.values():
        if (promedio < sum(promedioalto['notas'])/ len(promedioalto['notas'])):
            promedio = sum(promedioalto['notas'])/ len(promedioalto['notas'])
            estudiante = promedioalto
    print('El/La estudiante con mejor promedio fue ' + estudiante ['name'] + 'y obtuvo el promedio: ' + str(promedio))
    return promedio
 #PROMEDIO MÁS BAJO
def low_average():
    promedio = 10.0
    promediobajo = {}
    for estudiante in students.values():
        if promedio > sum(estudiante['notas'])/ len(estudiante['notas']):
            promedio = sum(estudiante['notas'])/ len(estudiante['notas'])
            promediobajo = estudiante
    print('El estudiante con el promedio más bajo fue: ' + promediobajo['name'] + ' con el promedio de: ' + str(promedio))
    return promedio
print(high_average())
print(low_average())
# NOTA MÁS ALTA


def high_grade():
    nota_alta = 0.0
    for nota_estudiante in students.values():
        for valor_nota in nota_estudiante['notas']:
            if nota_alta < valor_nota:
               nota_alta = valor_nota
    return nota_alta


def nota_repetida():
    for n_repetida in students.values():
        for nota in n_repetida['notas']:
           for i in students.values() :
               
               nota = n_repetida
        for revision in n_repetida['notas']:
            if revision == n_repetida:
                A=0

nota_repetida()