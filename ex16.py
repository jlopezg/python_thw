# -- coding: utf-8 --

from sys import argv

script, filename = argv

print "We' re going to erase %r. " % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If to do want that, hit RETurn."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "now I'm going to ask for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to be file."

target.write(line1 + "\n" +line2+ "\n" +line3)


print "and finally, we close it."
target.close()
