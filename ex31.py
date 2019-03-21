# -*- coding: utf-8 -*-

print "you enter a dark roon with two doors. Do you go thke through door #2?"

door = raw_input("> ")

if door == "1":
	print "there's a giant bear here eating a cheese cake. what do you do?"
	print "1. take the cake"
	print "2. Scream at the bear"

	bear = raw_input("> ")

	if bear == "1":
		print "the bear your eats face off. Good job!"
	elif bear == "2":
		print "the bear eats your legs off.  Good job!"
	else:
		print "well, doing %s is probably better. bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at cthulhu's retina."
	print "1. Blueberries"
	print "2. Yellow jacket closthesping"
	print "3. Understandig revolvers yelling melodies."

	insanity = raw_input("> ")


	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mid of jello. Good job!"
	else:
		print "The insanity rots you eyes int pool of muck. good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
