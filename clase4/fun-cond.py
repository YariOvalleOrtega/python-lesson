def verificar_mayor(edad_1, edad_2, edad_3, edad_4):
    if edad_1 >= edad_2 and edad_1 >= edad_3 and edad_1 >= edad_4:
        print('1' + str (edad_1))
    elif edad_2 > edad_3 > edad_4:
        print('2' + str(edad_2))
    elif edad_3 > edad_4:
        print('3' + str(edad_3))
    else:
        print('4' + str(edad_4))

verificar_mayor(15, 15, 10, 8)
verificar_mayor(15, 28, 25, 35)
verificar_mayor(65, 58, 45, 65)
#verificar_mayor(int(input('ingresa la edad 1:   ')),
# int(input('ingresa la edad 2:   ')),
# int(input('ingresa la edad 3:   ')),
# int(input('ingresa la edad 4:   ')) )

    