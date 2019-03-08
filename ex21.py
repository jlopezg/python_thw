# -- coding: utf-8 --

def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACTING %d - %d " % (a,b)
	return a - b

def multiply(a,b):
	print "MULTIPLY %d * %d" % (a,b)
	return a* b

def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b


print "let's do some math with just functions!"

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

print "age: %d, height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)


#A puzzle for the extra credit, type it in anyway.

print "here is puzzle."

what = add(age,subtract(height,multiply(weight, divide(iq,2))))

print "that become: ", what, "Can do you it by hand?"