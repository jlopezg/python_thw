# -*- coding: utf-8 -*-

from sys import argv

script, fileman = argv

txt = open(fileman)

print "Here's your file %r: " %fileman
print txt.read()

print "Type the fileman again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()