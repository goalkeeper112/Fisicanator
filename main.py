#!usr/bin/python

# Saludo y entrada del script en python desarrollado por Aponce y Goalkeeper112

print '#####################################################'
print '#######           Fisicanator               #########'
print '#######     Un srcipt para determinar       #########' 
print '####### la cantidad de calor de un objeto   #########'
print '#######                                     #########'
print '#######     Desarrollado Por Aponce y       #########'
print '#######          Goalkeeper112              #########'
print '#####################################################'

print 'Digite los valores necesarios para el calculo'

# En esta parte se digitan los datos numericos de la ecuacion

masa = input("masa: ")
t1   = input("temperatura Inicial: ")
t2   = input("temperatura final: ")
# En esta parte se pide la digitacion del material con el cual se esta trabajando

ce   = (raw_input("material: "))

if(ce == 'aluminio'):
	ce = 0.22
	q  = masa * ce * (t2 - t1)
	print q
else:
	print "No se puede resolver la ecuacion"
