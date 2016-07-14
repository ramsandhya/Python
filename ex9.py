# days = "Mon Tue Wed Thu Fri Sat Sun"

# \n gives a new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\n"
# print "Here are the days: ", days
# print "Here are the months: ", months
#
# # """ is used for multi lines
# print """
# There is something Here
# With the three double-quotes
# We'll be able to type as much as I could
# Even 4 line if we want, or 5, or 6.
# """
print months

# %s gives the value what user sees or prints
# prints
# Jan
# Feb
# Mar
# Apr
# May
# Jun
# Jul
# Aug

print "%s" % months


# %r is basically used for the debugging purpose for programmers so just gives out the value that variable has
# prints
# 'Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\n'
print "%r" % months
