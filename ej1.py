# -- coding: utf-8 --
import math
numero = int(input("Ingrese un Numero: "))
numero += 1
if numero > 0:
	for i in range(1,numero):
		raiz = math.sqrt(i)
		print  i,"raiz cuadrada: ",raiz
		
else:
	print "el numero ingresado no es entero"
		
	
