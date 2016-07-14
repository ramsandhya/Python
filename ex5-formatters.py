my_name = "Zed"
my_age = 35
my_height = 74
my_weight = 180
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about %s" % my_name
print "He's %d inches tall." % my_height
print "He's %d years old" % my_age
print "His eyes are %s" % my_eyes
print "His %d and %s make everybody smile and %s and %s" % (my_age, my_eyes, my_teeth, my_hair)

name = "Zed"
age = 35
height = 74
BMI = 74.36
weight = 180
eyes = "Blue"
teeth = "White"
hair = "Brown"
meters = 10

# These are formatters
print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d years old" % age
print "His eyes are %s" % eyes
print "His %d and %s make everybody smile and %s and %s" % (age, eyes, teeth, hair)
print "He's is %r " % age
print "%d " % round(BMI)

# it is concatenating the height 2 times
print "%d" % height * 2

# same behavior
print "%s" % height * 2

# printing the string
print "%s" % "height * 2"

# evaluating the expression
print "%d" % (height * 2)

# evaluating the expression
print "%s" % (height * 2)

# %d value is 4 like string interpolation in Swift
print "bla blah %d" % 4
