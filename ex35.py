from sys import exit

def gold_room():
	print "This room is full of gold. how much do you take?"
	
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
	    dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
	    dead("you greedy bastard!")
		
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "how are you going to move the bear?"
	bear_moved = false
	
	while true:
		next = raw_input("> ")
		
		if next == "take honey":
		    dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. you can go throungh it now."
			bear_moved = true
		elif next == "taunt bear" and bear_moved:
		    dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
		    gold_room()
		else:
		    print "I got no idea what that means."
			
			
def cthulhu_room():
	print "Here you see the grat evil cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
	    start()
	elif "head" in next:
	    dead("well that was tasty!")
	else:
	    cthulhu_room()
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
	print("verificacion de acceso")

edad_usuario=int(input("introduce tu edad, por favor "))

if edad_usuario<18:
	print("no puedes pasar")
else:
	print("puedes pasar")
print("el programa ha finalizado")
	
def start():
	print "you are in a dark room."
	print "There is a dood to your right and left."
	print "which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
	    bear_room()
	elif next == "right":
	    cthulhu_room()
	else:
	    dead("you stumble around the room until you starve.")
		
start()