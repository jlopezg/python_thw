# -- coding: utf-8 --

fomatter = "%r %r %r %r"

print fomatter % (1,2,3,4)
print fomatter % ("one", "two", "three", "four")
print fomatter % ( True, False, False, True)
print fomatter % (fomatter, fomatter, fomatter, fomatter)
print fomatter % (

	"I had this thing",
	"that you could type up right",
	"But it didn' t sing.",
	"So I said goodnight.")