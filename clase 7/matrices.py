lista= [ 5, 4, 6, 8]

matriz = [lista, lista, lista] #matriz es una lista de listas
matriz = [[ 5, 4, 6, 8], [ 5, 4, 6, 8], [ 5, 4, 6, 8]]

for fila in matriz:
    print(lista)

for fila in matriz:
    print(max(fila)) #el dato maximo de las listas
    print(min(fila)) #el dato minimo
    print(sum(fila)/len(fila)) #promedio

matriz = [[ 5, 4, 6, 8], [ 5, 4, 6, 8], [ 5, 4, 6, 8]]

print(matriz[0])
print(matriz[0][0])
print(matriz[1][0]) #nombre de la matriz, esa lista, posición de la lista
print(matriz[-1][-1]) #ultima lista, y ultima posición

for fila in matriz:
    for element in fila:
        print(element)
