formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)

#  don't forget the comma
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % ( formatter, formatter, formatter, formatter)

# don't forget the comma
print formatter % (
    "I had this thing",
    "That you could type up right",
    "But it didn't sing.",
    "So I said goodnight."
)

#  %r, %s and %d are the formatters
# %r is used for dubugging purpose
# %s and %d should be use appropriatey for string and decimals
