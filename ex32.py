# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for loop goes throught a list

for number in the_count:
	print "This is count %d" %number

# Same as above
for fruit in fruits:
	print " A fruit of type: %s" %fruit

# Also we can go throught mixed lists too
# Notice we have to use %r since we don't know whta's in it
for i in change:
	print "I got %r" %i

# we can also build lists, first statr with an empty one
elements = []

# The range function to do to 5 counts
for i in range(0,6):
	print "Adding %d to the list." %i
	# Append is a function that lists understand
	elements.append(i)

# Now we can print then out too
for i in elements:
	print 'Elements was: %d' %i