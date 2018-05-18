# -*- coding: cp1252 -*-
#Introducción de cantidad
mo=int(raw_input('Cantidad: $'))

#Comenzar la división monetaria
#Dividir entre 500
if mo >= 500:
    q=mo/500
    print'%d monedas de $500' %q
    mo-=(500*q)
    
#Dividir entre 200
if mo >= 200:
    q=mo/200
    print'%d monedas de $200' %q
    mo-=(200*q)
    
#Dividir entre 100
if mo >= 100:
    q=mo/100
    print'%d monedas de $100' %q
    mo-=(100*q)
    
#Dividir entre 50
if mo >= 50:
    q=mo/50
    print'%d monedas de $50' %q
    mo-=(50*q)
    
#Dividir entre 20
if mo >= 20:
    q=mo/20
    print'%d monedas de $20' %q
    mo-=(20*q)
    
#Dividir entre 10
if mo >= 10:
    q=mo/10
    print'%d monedas de $10' %q
    mo-=(10*q)
    
#Dividir entre 5
if mo >= 5:
    q=mo/5
    print'%d monedas de $5' %q
    mo-=(5*q)
    
#Dividir entre 2
if mo >= 2:
    q=mo/2
    print'%d monedas de $2' %q
    mo-=(2*q)
    
#Dividir entre 1
if mo >= 1:
    q=mo/1
    print'%d monedas de $1' %q
    mo-=(1*q)
