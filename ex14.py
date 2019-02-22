# -- coding: utf-8 --

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I;m the %s script." % (user_name,script)
print "I'd like to ask you a few questions.wh"
print "do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "Where do you computer do you have?"
Computer = raw_input(prompt)

print """
alright, so you said %r about liking me.
you live %r. not sure where that is.
And you have %r computer. nice.
""" % (likes,lives,Computer)