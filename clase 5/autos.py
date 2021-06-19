autos = {'autos': {
        1: {'Marca': 'tesla',
            'modelos': {
               1:'Model S',
               2:'Model E',
               3:'Model X',
               4:'Model Y',
                }
            },
        2: {'Marca':'Toyota',
            'modelos': {
               1:'Fortuner',
               2:'Prado',
               3:'Tundra',
               4:'Corola',
                }
            },
        3: {'Marca':'Range Rover',
            'modelos': {
                1:'Evoque',
                2:'Defender',
                }
            },
        4: {'Marca':'Mazda',
            'modelos': {
               1:'Mazda 3',
               2:'Mazda 2',
               3:'CX 30',
                }
            },
        5: {'Marca':'Audi',
            'modelos': {
               1:'A7',
               2:'A5',
               3:'A3',
                }
            }
                    }
        }


#cuarto modelo de la marca tesla
# print(autos['autos'][1])
# print(autos['autos'][1]['modelos'][4])
# print(autos['autos'][3]['modelos'][2])

#cual marca es la tiene mas modelos

M1 = len(autos['autos'][1]['modelos'])
M2 = len(autos['autos'][2]['modelos'])
M3 = len(autos['autos'][2]['modelos'])
M4 = len(autos['autos'][2]['modelos'])
M5 = len(autos['autos'][2]['modelos'])

if M1 >= M2 and M1 >= M3 and M1 >= M4 and M1 >= M5:
    print('Tesla tiene más modelos')
elif M2 >= M3 and M2 >= M4 >= M5:
    print('Toyoya tiene más modelos')
elif M3 >= M4 and M4 >= M5:
    print('Range Rover tiene más modelos')
elif M4 >= M5:
    print('Mazda tiene más modelos')
else:
    print('Audi tiene más modelos')