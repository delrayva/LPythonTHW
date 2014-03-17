from sys import argv
from time import sleep

script, user_name, password = argv
prompt = "something else entirely"

print "Hi %s, I'm the %s script." % (user_name, script)
print "You entered %s for your password," % (password),
print "I don't recognize that."
print "I'd like to ask you a few questions."
print "..."
sleep(3)
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
