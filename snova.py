# -*- coding: cp1252 -*-
opc=''

while opc != 'n':
    a=str(raw_input('Press ->'))
    a1=ord(a)
    print'Valor -> %d \n/23 = %d \nmod23 = %d' %(a1,a1/23,a1%23)
    opc=str(raw_input('Más datos: '))
