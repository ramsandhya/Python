from sys import argv
script, user_name = argv
zed = " uiui"

print "Hi %s, I'm the %s script." %(user_name, script)
print "Do you like me %s ?" % user_name
likes = raw_input()

print "Where do you live %s?" % user_name
lives = raw_input()

print "What kind of computer do you have?"
computer = raw_input()

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

# What is the prompt variable and its use?
