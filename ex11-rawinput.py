# print "How old are you?",
# age = 9
# print "How tall are you?",
# height = 10
# print "How muxh do you weigh?",
# weight = 11
#
# print "So you are %d old, %d tall and %d heavy" % (age, height, weight)

# prints input in line 11, put the name, says line 12 with name, prints line 13
# name = raw_input("What is your name?")
# print "Hello %r" % name
# print '6\'2"'

# Whatever we put in the prompt we get the outpit based on the %s and %d. if we put %r it will give th eresult in single quotes.
# name = raw_input("What is your name?")
# age = raw_input("How old are you?")
# print "Welcome %s , you are %rjane years old" % (name, age)

# The value we enter is getting converted to the integer so 40 will work but 6'5" will not
x = int(raw_input())
print x

# In order for 6'5" to work we need to take int off
x = raw_input()
print x
