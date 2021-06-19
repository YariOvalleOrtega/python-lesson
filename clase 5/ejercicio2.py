numeros = [54, 58+5, 45, 12, 57, 84, 64, 25]

# for numero in numeros:
#     if numero > 50:
#         print(numero)

# for numero in numeros:
#     if numero % 2 == 0: #divide al numero por dos y si el residuo es igual a 0 muestra el numero
#         print(numero)
#     else: 
#         print('-')

i= 0
menor = 0 

while i < len(numeros):
    if i == 0:
        menor = numeros[i]
    if menor < numeros [i]:
        menor = numeros [i]
    i += 1
print(menor)