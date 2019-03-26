# -*- coding: utf-8 -*-

from sys import exit

def camino1():
	print 'Este es el camino hacia el bosque. Quieres entrar?'

	next = raw_input('> ')
	if "0" in next or "1" in next:
		how_much = int(next)

	else:
		dead("Hey, escribe un numero.")

	if how_much < 50:
		print "Bien, sigue adelante"
		exit(0)
	else: 
		dead("Pues no puedes seguir, bai.")


def lobo():
	print "Aqui hay un lobo."
	print "El lobo se esta comiendo un trozo de carne."
	print "El lobo te comera si continuas." 

	
	lobo_mover = False

	while True:
		next = raw_input('> ')

		if next == "Tomar la carne":
			suerte(" El lobo esta viendote para atacarte.")


		elif next == "Caminar" and not bear_moved:
			print "Si te mueves mueres."
			lobo_mover = True


		elif next == "Carne" and lobo_mover:
			suerte("Arrojar carne y correr.")


		elif next == "Abrir puerta" and lobo_mover:
			camino1()


		else:
			print "No se que hacer."

def camino2():
	print "Aqui esta tu ex."
	print "Tu ex toxica/o quiere regresar contigo."
	print "Quieres regresar con el/ella o salir corriendo?"

	next = raw_input('> ')

	if "correr" in next:
		start()


	elif "regresar" in next:
		suerte("Han regresado.")


	else:
		camino2()


def suerte(why):
	print why, "Muy Bien!"
	exit(0)



def start():
	print "Estas en la habitacion del terror"
	print "Aqi hay dos puertas, derecha e izquierda"
	print "Cual eliges?"

	next = raw_input('> ')

	if next == 'izquierda':
		camino1()


	elif next == 'derecha':
		camino2()


	else:
		suerte("Mi loco suelta esa loca, deja eso.")


start()
