# -*- coding: cp1252 -*-
num=int(raw_input('Teclea un n�mero: '))

primo=True
divisor=2

#for divisor in range(2, num):
while divisor < num and primo:
    if num % divisor == 0:
        primo=False
    divisor+=1

if primo:
    print'El n�mero:',num,'es primo'
else:
    print'El n�mero:',num,'no es primo'
