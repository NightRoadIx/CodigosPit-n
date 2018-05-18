valor=10

cad='*'
for i in range(1,valor):
    print cad
    cad+='*'

for i in range(1,9):
    print cad[1:len(cad)-i]
