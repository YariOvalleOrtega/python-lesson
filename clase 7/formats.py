num1 = 45
num2 = 36

mensaje = 'Los números son ' + str(num1) + ' , ' + str(num2)
print(mensaje)

mensaje = 'Los números son {}, {}'.format(num1,num2)
print(mensaje)

mensaje = 'Los números son {1}, {0}'.format(num1,num2)
print(mensaje)

mensaje = 'Los números son {1}, {0}, {2}'.format(num1,num2, 58)
print(mensaje)

mensaje = 'los números son %d, %d'%(num1, num2)
print(mensaje)

mensaje = f'Los números son {num1}, {num2}'
print(mensaje)