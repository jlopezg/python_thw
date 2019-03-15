# -*- coding: utf-8 -*-

# this one is like yoyr scripts with argv
def print_two(*args):
	arg1, arg2, arg3 = args
	print "arg1: %r, arg2: %r, arg3: %r" %(arg1, arg2, arg3)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
	print "I got nothing'."
	

print_two("Zed","Shaw","Mendez")
print_two_again("Zed","Shaw")
print_one("First!")
print_none() 

#name = raw_input("Nombre")
#last_name = raw_input("apellido")
#age = raw_input("edad")
#print_two(name, last_name, age)
