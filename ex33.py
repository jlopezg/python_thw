i = 0
numbers = []

num = int(input("Elija un numero: "))

while i < 6:
	print([i for i in [0, 1, 2, 3, 4, 5, 6,] if i < num])
	#print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
	
print "The numbers: "

for num in numbers:
	print num 