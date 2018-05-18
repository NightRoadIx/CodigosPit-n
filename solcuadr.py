# -*- coding: cp1252 -*-
from math import sqrt

a=float(raw_input('Valor de a: '))
b=float(raw_input('Valor de b: '))
c=float(raw_input('Valor de c: '))

if a != 0:
    discriminante=b**2 - 4*a*c
    if discriminante >= 0:
        x1=(-b + sqrt(discriminante)) / (2*a)
        x2=(-b - sqrt(discriminante)) / (2*a)
        if x1 == x2:
            print'Solución de la ecuación: \n%4.3f' %x1
        else:
            print'Soluciones de la ecuación: \nx1=%4.3f \nx2=%4.3f' %(x1,x2)
    else:
        print'No hay soluciones reales'
else:
    if b != 0:
        x=-c/b
        print'Solución de la ecuación: \nx=%4.3f' %x
    else:
        if c!= 0:
            print'La ecuación no tiene solución'
        else:
            print'La ecuación tiene infinitas solución'
