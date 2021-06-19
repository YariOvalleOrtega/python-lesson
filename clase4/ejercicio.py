#valor por consola

#si ese valor esta dentro de un rango
#si esa persona pertenece a una categoria
#si esta dentro de 10-14  años es categoria infantil
#15-17 es juvenil
#18-20 sub veinte
#mayor de 20 profesional

edad = int(input('ingresa tu edad: '))

#if edad <= 14 and edad >= 10: 
#    print('Eres categoria infantil')
#elif edad <= 17 and edad >= 15:
#    print('Eres de categoria juvenil')
#elif edad <= 20 and edad >= 18:
#    print('Eres de categoria sub-20')
#elif edad > 20:
#    print('Eres profesional')
#else:
#    print('Eres menor')

if edad > 20: 
    print('Eres profeesional')
elif edad >= 18:
    print('Eres de categoria sub-20')
elif edad >= 15:
    print('Eres de categoria juvenil')
elif edad >= 10:
    print('Eres de categoria infantil')
else:
    print('Eres menor')


