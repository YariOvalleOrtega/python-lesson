"""
    Un bus viaja a 30km/h en promedio, 90km
    recoger pasajeros demora 2 minutos por pasajero
    bajar pasajero demora 1 minuto

    Cuantos minutos demora el bus, dada una cantidad de pasajeros que se subieron
    y otra cantidad de pasajeros que se bajaron
"""

def tiempo_recorrido_bus(numero_abordados, numero_descendidos):
    recorrido_total = 180 
    return recorrido_total
print(tiempo_recorrido_bus ((int(input('ingrese numero abordados: ')*2)), (int(input('ingrese numero de desceos: ')*1)) + 180)) 


def calcular_tiempo_recorrido(numero_abordados, numero_desc):
    tiempo = (90 / 30) * 60
    tiempo_subieron = numero_abordados * 2
    tiempo_bajaron = numero_desc * 1
    return int(tiempo_subieron + tiempo_bajaron + tiempo)
Cant_recogidos = int(input("Digite numero de pasajeros recogidos: "))
cant_descendidos = int(input("Digite numero de pasajeros que descendieron: "))
print("El autobus tardo ", calcular_tiempo_recorrido(cant_descendidos, Cant_recogidos)," minutos")