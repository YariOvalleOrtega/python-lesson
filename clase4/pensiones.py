edad = 58 
genero = 'F'
semanas = 240

# if edad >= 58 and genero == 'F' and semanas >= 240:
#     print('Se puede pensionar')
# else:
    # print('No se puede pensionar')

#ANIDACIÓN
def pension(genero,edad,semanas):
    if genero == 'F':
         if edad >= 58:
            if semanas >= 240:
                 print('Se puede pensionar')
            else:
                print('Le faltan ' + str(240 -semanas)+ ' semanas')
         else:
            print('le faltan ' + str( 58 - edad)+ ' años')
    elif genero == 'M':
        if edad >= 63:
            if semanas >= 240:
                print('Se puede pensionar')
            else:
                print('Le faltan ' + str(240 -semanas)+ ' semanas')
        else:
            print('le faltan ' + str( 63 - edad)+ ' años')
    else:
        print('Genero no valido')

pension(str('h'), 58, 230)