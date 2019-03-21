print "you enter a dark room with two doors. do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "there's a giant bear here eating a cheese cake. what do you do?"
	print "1. take the cake."
	print "2. scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
	    print "the bear eats your face off. Good job!"
	elif bear == "2":
	    print "The bear eats your legs off. Good job!"
	else:
	    print "well, doing %s is probably better. bear runs away." % bear
		 
elif dood == "2":
	print "you stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
	    print "Your body survives powered by a mind of jello. Good job!"
	else:
	    print "The insanity rots your eyes into a pool of muck. Good job!"
		
else:
    print "you stumble around and fall on a knife and die. Good job!"