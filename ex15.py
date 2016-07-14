#  We get input from the user by raw_input from running command line
#  And by command line itself through argv

# only raw_input gets a string. needs to be converted to int
# x = int(raw_input())
# y = 4
# print "%r" % x
# print "%r" % y
# print "%r" % (x + y)

# we are using argv module
from sys import argv

# we need 2 arguments in the command line
script, filename = argv

# we are reading the file in the background with open function
text = open(filename)

# prints the filename i.e. ex15_sample.txt
print "Here's your file %r" % filename

# prints the contents of the file with read function
print text.read()

print "Tyoe the filename again: "

# asks for an input from user, prompts > sign, asigns that value to the file_again variable we enter ex15_sample.txt
file_again = raw_input(">")

# prints the filename i.e. ex15_sample.txt
txt_again = open(file_again)

# prints the contents of the file
print txt_again.read()


# What is pydoc open?
