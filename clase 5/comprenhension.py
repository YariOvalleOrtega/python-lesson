notas = [ 3.1,4.2,4,3.9,3.2]

#de una lista sacar otra lista
#por cada elemento en un literable se guarda el elemento si se cumple una condicion
notas_c = [nota for nota in notas if nota > 3.5]
#notas_c = [nota*2 for nota in notas if nota > 3.5]
print(notas_c)