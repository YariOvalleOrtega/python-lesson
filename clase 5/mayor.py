#promedio mas alto dentro de una función
numeros1 = [59, 58+5, 45-5, 12*2]
numeros2 = [54, 58+5, 45, 12+24]
numeros3 = [54+2, 58+5, 45, 12]
numeros4 = [4, 58+5, 45*2, 12]
# podria ser promedio_1 = sum(numeros1)/ len(numeros1)
promedio_1 = sum(numeros1)/4
promedio_2 = sum(numeros2)/4
promedio_3 = sum(numeros3)/4
promedio_4 = sum(numeros4)/4

def promedio():
    if promedio_1 >= promedio_2 and promedio_2 >= promedio_3 and promedio_3 >= promedio_4:
        print ('Promedio 1 es mayor')
    elif promedio_2 >= promedio_3 and promedio_3 >= promedio_4:
        print('Promedio 2 es mayor')
    elif promedio_3 >= promedio_4:
        print('promedio 3 es mayor')
    else:
        print ('promedio 4 es mayor')
 
promedio()
