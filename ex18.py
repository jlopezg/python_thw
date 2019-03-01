# -- coding: utf-8 --

# this one is like scripts with argv
def print_two(*argvs):
	arg1,arg2 = argvs
	print "arg1: %r, arg2: %r" %(arg1, arg2)

	#ok, that *args is actually pointless, we can ust do this
def print_two_again(arg1,arg2):
	print "arg1: %r,arg2: %r " % (arg1, arg2)

#this ust tkes one argument
def print_one(arg1):
	print "arg1: %r" %arg1

#this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first!")
print_none()

      
