# -*- coding: cp1252 -*-
#Se crea la lista
a = [1, 2, -1, -4, 5, -2]

#Se inicia el index
i = 0
#Ahora hay que actualizar la longitud de la lista
while i < len(a):
    #Cuando sea negativo el número lo borra
    if a[i] < 0:
        del a[i]
    #En otro caso incrementa el indice
    else:
        i += 1

print a
