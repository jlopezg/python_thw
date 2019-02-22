# -- coding: utf-8 --

tabby_cat="\ti'm tabbed in"
persian_cat = "i'M split\non a line"
backslash_cat= "I'm\ a \ cat"

fat_cat = """
I'll do a list:
\t* cat food
\t* Fishies
\t* Cat\n\t* grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,