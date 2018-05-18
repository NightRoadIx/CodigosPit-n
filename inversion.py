# -*- coding: cp1252 -*-
cadena = raw_input('Introduce una cadena: ')

inversion = ''
for caracter in cadena:
    inversion = caracter + inversion

print 'Su inversión es:', inversion
