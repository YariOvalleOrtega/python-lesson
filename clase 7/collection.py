palabra = 'Una palabra'
print(palabra)

lista = list(palabra)
print(lista)

diccionario = {'nombre' : 'Yaritza', 'apellido' : 'Ovalle'}
lista = list(diccionario) #cuando el diccionario se convierte en lista solo devuelve sus iterables
print(lista)
lista = list(diccionario.keys()) #cuando el diccionario se convierte en lista solo devuelve sus iterables
print(lista)
lista = list(diccionario.values()) 
print(lista)
lista = list(diccionario.items()) #lo devuelve en tuplas
print(lista)
tupla = tuple(lista)
print(tupla)

#--------------
palabra = 'Una palabra'
lista= list(palabra)
palabra = ''.join(lista)
print(palabra)