#sueldo = int(input('digite su sueldo:   '))
#sueldo= int(sueldo)
#print('su sueldo es ' + str(sueldo+200000))
#def sumar_numeros(): 
#    print(65+64)

#sumar_numeros()
#numero = 10
#def calcular_numero(numero):
#    print(numero*2)

#def calcular_cuadrado(numero): 
#    print(numero*numero)

#calcular_cuadrado(int(int(input('digite su numero: '))))

def calcular_total(num1, num2, num3) -> int:
    total_local= num1 + num2 + num3
    return total_local 

def promedio ():
    numero_1 = int(input('ingrese numero 1:  '))
    numero_2 = int(input('ingrese numero 2:  '))
    numero_3 = int(input('ingrese numero 3:  '))
    total = calcular_total(numero_1, numero_2, numero_3)
    return total/3 
print(promedio())
