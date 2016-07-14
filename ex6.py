x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who don't know %s and who %s" % (binary, do_not)
print x
print y
print "I said: %r" % x

# If i put %d instead of %s then it will give an error
# %d is used for numbers
# %s is used for string
# %r will give results when used with %s or %d
print "I also said %d" % y


# hillarious = False
# joke_evaluation = "Ian't that joke so funny %r" % hillarious
#
# # prints the value evaluated out of hillarious variable
# print joke_evaluation % hillarious
# w = "This is the left side of.."
# e = "a string with right side "
#
# # concatenates the string
# print w + e
