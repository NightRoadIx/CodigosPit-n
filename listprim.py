# -*- coding: cp1252 -*-
n=int(raw_input('Teclea un número: '))

#Creamos la lista vacía
primos=[]
for i in range(2,n+1):
    #Determinamos si i es primo
    creo_es_primo=True
    for divisor in range(2,i):
        if i % divisor == 0:
            creo_es_primo=False
            break

    #Y si es primo se añade a la lista
    if creo_es_primo:
        primos.append(i)

print primos
