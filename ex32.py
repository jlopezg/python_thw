# -*- coding: utf-8 -*-


the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pear', 'apricors']
chage = [1, 'pennies', 2 ,'dimes', 3, 'quarters']

#this first kind of for -loop goes through a list


for number in the_count:
	print "this is count %d" % number


#same as above

for fruit in fruits:
	print "A fruit of type: %s" % fruit

	#also we can through mixed liss too
	#notice we have to use %r since we don't know what's in it

for i in chage:
	print "I got %r" % i


#we can also build list,first start with an empty one
elements = []

# then use range funtions to do 0 to 5 counts
for i in range(0,6):
	print "adding %d to the list. "% i
	# append is a funtions that list understand
	elements.append(i)

# now we can print them out too

for i in elements:
	print "Element was : %d" % i