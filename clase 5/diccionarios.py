#diccionario cuando se crea se usan {}
#cuando se quiere acceder se usa []
#clave debe ser unica, se llama es la clave
# diccionario = {'clave': 'valor'}
# diccionario = {'nombre1': 'yaritza', 'edad1': 24,
#                'nombre2': 'liliana', 'edad2': 54}

# print(diccionario['nombre'])


diccionario = {'nombre1': 'yaritza',
                'edad1': 24,
                'lenguajes': {1: 'python',
                              2: 'C++',
                              3: 'Java',
                              4: 'PHP',
                              5: 'Javascript',
                              6: 'C#'}
               }
#print(diccionario ['lenguajes'][4])
# LEN CONTAR LOS ELEMENTOS DE UN DICCIONARIO
#print(len(diccionario))
#print(len(diccionario['lenguajes']))

diccionario['nombre1']
print(diccionario.keys()) #cuantas llaves hay
print(diccionario.values())
print(diccionario.items()) #devuelve los items