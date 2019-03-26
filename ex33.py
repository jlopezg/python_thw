# -*- coding: utf - 8 -*-

v = raw_input("intoduzca un numero: ")

numbers = []

def items(v):

	i = 0
	
	while i < int(v) :
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "numbers now", numbers

		print "at the botton i is %d" % i

items(v)
 
print "the numbers: "

for num in numbers:
	print num