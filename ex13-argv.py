from sys import argv
# script, first, second, third = argv
# print "The script is called", script
# print "The first variable is called ",first
# print "The second variable is called", second
# print "The third variable is called", third

# argv needs these arguments from the command line. The first argument will be the name of the script. nachos, sandwich, fries are all variables.
#  Command line will take 1st argument as the script.py which is ex13.py and the other 4 arguments as there are 4 other arguments.
# The command line returns string so if we need to add the arguments convert themto integer by int method
#  From the book - "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order."


# script, nachos, sandwich, fries, dessert = argv
# print script
# print nachos
# print sandwich
# print fries
# print dessert
#
# # same as print nachos
# print raw_input(nachos)

# concatenates
# print nachos + sandwich

# prints added values
# print (int(nachos) + int(sandwich))

# prints input we give in command line after it runs
print raw_input()

# argv takes inputs at command line not after it runs
