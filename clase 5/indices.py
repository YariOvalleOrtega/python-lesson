#indices
# palabra.replace remplaza una letra por otra
palabra = 'un texto de varias palabras'

# print(palabra[0])
# print(palabra[1])
# print(palabra[2])
# print(palabra.replace ('a', 'o'))
# print(palabra.replace ('a', 'o', 1)) #cuantas se quieren cambiar

#slice permiten acceer o hacer que el texto se corte en rebanadas -  sacar una parte del texto

print(palabra[4:10]) #posicion 4 hasta la 10, el último valor no se incluye
print(palabra[0:8])
print(palabra[:8])
print(palabra[:])
print(palabra[-5:-2])
print(palabra[: : 2]) #saltando de 2 en 2
print(palabra[: : -1]) #el texto al reves