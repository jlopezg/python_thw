# -*- coding: utf-8 -*-



num = int(raw_input('>  ' ))
numbers = []
def bucle(num):
	i = 0

	while i < int(num):

		print "At the top i is %d" % num
		numbers.append(i)

		i = i + 1
		print "numbers now: ", numbers
		print "At the bottom i is %d" % i

bucle(num)

print 'The numbers: '

for num in numbers:
	print num