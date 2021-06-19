
# El promedio más alto high_average
# def high_average(students):
#     prom_mayor = 0
#     for student in students.values():  
#         prom_stud = sum(student['notas']) / len(student['notas'])
#         if prom_stud > prom_mayor:
#             prom_mayor = prom_stud
#     print ("El promedio más alto es: " + str (prom_mayor))



#Promedio más alto
promedio =0.0 
E_promedio = {}
for estudiante in students.values():
    # promedio = (sum(estudiante['notas']) / len(estudiante['notas']))
    if(promedio<((sum(estudiante['notas']) / len(estudiante['notas'])))):
        promedio = sum(estudiante['notas']) / len(estudiante['notas'])
        E_promedio = estudiante
print("El Estudiante con promedio más alto es: ",E_promedio['name'],"con un promedio de: ",promedio)

#---------
promediomenor=100
notamayor=0
notamenor=100
for key, value in students.items():
    # print(value['name'])
    promedio=sum(value['notas'])/len(value['notas'])
    for n in value['notas']:
        if n>notamayor:
            notamayor=n
            snmayor=value['name']
        if n<notamenor:
            notamenor=n
            snmenor=value['name']
    # print(promedio)
    if promedio>promediomayor:
        promediomayor=promedio
        smayor=value['name']
    if promedio<promediomenor:
        promediomenor=promedio
        smenor=value['name']




        estudiante = {'notas' : 0.0}
for nota in students.values():
    if nota ['notas'] >= estudiante['notas']:
        estudiante  = nota
    
print(estudiante ['name'], estudiante)