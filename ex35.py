# -*- coding :utf - 8 -*-
from sys import exit

def gold_room():
	print "this room is full gold. How much do you takes?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
	 		how_much = int (next)
	else:
	 		dead("man, learn to type a number.")

	if how_much < 50:
	 		print "nices you're not greedy, you win!"
	 		exit(0)

	else:
	 		dead("you greedy bastard!")



def bear_room():
 print "There is bear here."
 print "There bear has bunch of heney."
 print "The 	fat bear is in front of another door"
 print "How are you goint to move the bear?"
 bear_moved = False

 while True:
 	next = raw_input("> ")
 	if next == "take honey":
 			dead ("The bear looks at you slaps your face off")
 	elif next == "Taunt bear" and not bear_moved:
 		print "The bear has moved from the door. You can go through it now."
 		bear_moved = True
 	elif next == "Taunt bear" and  bear_moved:
 		dead("the bear gets pissed of and chews your leg off.")
 		gold_room()
 	else:
 		print "I got no idea what that means"



def cthulhu_room():
 print "Here you see the great evil Cthulhu."
 print "He, it , whateever stares at you and you go insane."
 print "Do you flee for your life or eat yout head?"

 next = raw_input("> ")

 if "flee" in next:
 	start()
 elif "head" in next:
 	dead("well that was tasty!")
 else:
 	cthulhu_room()


def dead(why):
 print why, "Good job!"
 exit (0)

def start():
 print "you are in a dark room"
 print "There is a door to your right and left"
 print "which one do you take?"

 next = raw_input ("> ")

 if next == "left":
 	bear_room()
 elif next == "right":
 	cthulhu_room()

 else:
 	dead ("you stumble around the romm until you starve.")

start()
