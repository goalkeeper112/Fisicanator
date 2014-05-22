#!usr/bin/python

# Saludo y entrada del script en python desarrollado por Aponce y Goalkeeper112

print '#################################################################'
print '#######                Fisicanator                      #########'
print '#######           Un srcipt para Resolver               #########' 
print '#######    La mayoria de los problemas planteados       #########'
print '#######        en la fisica 1 de Bachillerato           #########'
print '#######                                                 #########'
print '#######         Desarrollado Por Aponce y               #########'
print '#######              Goalkeeper112                      #########'
print '#################################################################'

tema = (raw_input("Tema a resolver: "))

if(tema == "calor"):
	# En esta parte se digitan los datos numericos de la ecuacion
	masa = input("masa: ")
	t1   = input("temperatura Inicial: ")
	t2   = input("temperatura final: ")
	# En esta parte se pide la digitacion del material con el cual se esta trabajando
	ce   = (raw_input("material: "))

	if(ce == 'aluminio'):
		medida = (raw_input("Con cual unidad va a trabajar: "))
		if(medida == "j"):
			ce = 898
			q  = masa * ce * (t2 - t1)
			print q
		elif(medida == "cal"):
			ce = 0.22
			q  = masa * ce * (t2 - t1)
			print q
		else:
			print "No se pudo resolver la ecuación debido a que ocurrio un error"
	elif(ce == 'cobre'):
		medida = (raw_input("Con cual unidad va a trabajar:"))
		if(medida == "j"):
			ce = 385
			q  = masa * ce * (t2 - t1)
			print q
		elif(medida == "cal"):
			ce = 0.09
			q  = masa * ce * (t2 - t1)
			print q
		else:
			print "No se pudo resolver la ecuación debido a que ocurrio un error"
	elif(ce == "plomo"):
		medida = (raw_input("Con cual unidad va a trabajar:"))
		if(medida == "j"):
			ce = 125
			q  = masa * ce * (t2 - t1)
			print q
		elif(medida == "cal"):
			ce = 0.03
			q  = masa * ce * (t2 - t1)
			print q
		else:
			print "No se pudo resolver la ecuación debido a que ocurrio un error"
	elif(ce == "aceite"):
		ce = 0.47
		q  = masa * ce * (t2 - t1)
		print q 
	else:
		print "No se puede resolver la ecuacion"
